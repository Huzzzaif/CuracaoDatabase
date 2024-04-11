from django import forms
from .userAuth_model import User  # Corrected import statement to use relative import

class SignupForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ['email', 'name', 'role', 'department', 'password']

    def save(self, commit=True):
        user = super(SignupForm, self).save(commit=False)  # Explicitly called super with class and self
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user