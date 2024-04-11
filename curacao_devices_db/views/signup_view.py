from rest_framework import generics, status
from rest_framework.response import Response
from django.contrib.auth.hashers import make_password
from curacao_devices_db.models import User
from curacao_devices_db.serializer import SignupSerializer

class SignupView(generics.CreateAPIView):
    serializer_class = SignupSerializer

    def post(self, request, *args, **kwargs):
        data = request.data
        data['password'] = make_password(data['password'])
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def get(self, request, *args, **kwargs):
        email = request.query_params.get('email')
        if not email:
            return Response({"error": "Email is required"}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            user = User.objects.get(email=email)
            # Assuming 'role' is a field in your User model
            return Response({"email": user.email, "role": user.role}, status=status.HTTP_200_OK)
        except User.DoesNotExist:
            return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)