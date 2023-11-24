from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import AbstractUser, PermissionsMixin
from django.core import validators
from django.db import models

from petstagram.accounts.managers import CustomAuthUserManager


# class Test(AbstractUser):
#     pass


class CustomPhoneNumberField(models.CharField):

    def to_python(self, value):

        if len(value) != 10:
            return "Phone number needs to be exactly 10 digits!"

        return value


class AuthUser(AbstractBaseUser, PermissionsMixin):

    email = models.EmailField(
        unique=True,
        null=False,
        blank=False
    )

    is_staff = models.BooleanField(
        default=False
    )

    USERNAME_FIELD = 'email'

    objects = CustomAuthUserManager()


class ProfileUser(models.Model):

    first_name = models.CharField(
        max_length=100,
        validators=[
            validators.MinLengthValidator(2, message="Your name needs consist of at least 2 letters!")
        ]
    )

    last_name = models.CharField(
        max_length=100,
        validators=[
            validators.MinLengthValidator(2, message="Your name needs consist of at least 2 letters!")
        ]
    )

    age = models.PositiveIntegerField()

    phone_number = CustomPhoneNumberField()

    user = models.OneToOneField(
        to='AuthUser',
        on_delete=models.CASCADE
    )
