from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

from django.utils import timezone


class MyUserManager(BaseUserManager):

    # fieldsets = UserAdmin.fieldsets + (
    #     (None, {'fields': ('custom_field',)}),
    # )
    def create_user(self, email, username, password=None, **extra_fields):
        if not email:
            raise ValueError('User Must have an email address')
        email = self.normalize_email(email)
        user = self.model(email=email,username=username,**extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, username, password,**extra_fields):
        user = self.create_user(email, username, password,**extra_fields)
        user.is_superuser = True
        user.is_staff = True
        user.save()
        return user


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=200, unique=True)
    username = models.CharField(max_length=20)

    first_name = models.CharField(max_length=20,null=True,blank=True)
    last_name = models.CharField(max_length=200,null=True,blank=True)

    date_joined = models.DateTimeField(default=timezone.now)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    # date_joined = models.DateTimeField(auto_now_add=True)

    ordering = ('email',)

    objects = MyUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def get_full_name(self):
        return self.username

    def get_short_name(self):
        return self.username

    def __str__(self):
        return self.email
