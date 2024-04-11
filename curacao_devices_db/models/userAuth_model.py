from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from django.utils import timezone


class UserManager(BaseUserManager):

  # This section includes methods for creating users and superusers, along with the User model definition.
  # The User model includes the following columns:
  # - email: EmailField, unique identifier for the user. This field is required and must be unique.
  # - name: CharField, optional name of the user. This field is not required and can be left blank.
  # - role: CharField, defines the role of the user within the system. Choices are limited to predefined roles.
  # - department: CharField, specifies the department the user belongs to. This is a free text field.
  # - is_active: BooleanField, indicates if the user account is active. Defaults to True.
  # - last_login: DateTimeField, tracks the last login time. This field can be null and is optional.
  # - date_joined: DateTimeField, records when the account was created. Automatically set to the current date and time when the account is created.

  def _create_user(self, email, password, role, department, **extra_fields):
    if not email:
        raise ValueError('Users must have an email address')
    if role not in ['Developer','Admin','Technician']:
        raise ValueError('Invalid role specified')
    now = timezone.now()
    email = self.normalize_email(email)
    user = self.model(
        email=email,
        role=role,
        department=department,
        is_active=True,
        last_login=now,
        date_joined=now,
        **extra_fields
    )
    user.set_password(password)
    user.save(using=self._db)
    return user

  def create_user(self, email, role, department, password=None, **extra_fields):
    extra_fields.setdefault('is_superuser', False)
    return self._create_user(email, password, role, department, **extra_fields)

  def create_superuser(self, email, password, role, department, **extra_fields):
    extra_fields.setdefault('is_superuser', True)
    extra_fields.setdefault('is_staff', True)

    if extra_fields.get('is_superuser') is not True:
        raise ValueError('Superuser must have is_superuser=True.')
    if extra_fields.get('is_staff') is not True:
        raise ValueError('Superuser must have is_staff=True.')

    return self._create_user(email, password, role, department, **extra_fields)

class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=254, unique=True)
    name = models.CharField(max_length=254, null=True, blank=True)
    role = models.CharField(max_length=10, choices=[('developer', 'Developer'), ('admin', 'Admin'), ('technician', 'Technician')])
    department = models.CharField(max_length=30,blank=True, null=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)  # Added for superuser
    last_login = models.DateTimeField(null=True, blank=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    

    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = ['role', 'department']  # Updated to include role and department

    objects = UserManager()

    def get_absolute_url(self):
        return "/users/%i/" % (self.pk)
