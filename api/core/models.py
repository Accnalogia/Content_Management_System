""" Core Model """
import uuid

from django.db import models
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _


class BaseModelMixin(models.Model):
    """ Abstract Model to be extended by all other models """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, max_length=32)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class EmailUserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, username, email,
                     password, **extra_fields):
        """
        Creates and saves a User with the given username, email and password.
        """
        if not username:
            raise ValueError('The given username must be set')
        email = self.normalize_email(email)
        username = self.model.normalize_username(username)
        user = self.model(
            username=username, email=email,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, username,
                    email, password, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(username, email, password,
                                 **extra_fields)

    def create_superuser(self, username, email, password,
                         **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(username, email, password,
                                 **extra_fields)


class EmailAbstractUser(AbstractUser, BaseModelMixin):
    email = models.EmailField(unique=True,)
    objects = EmailUserManager()

    REQUIRED_FIELDS = ['email']

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')
        abstract = True


class CMSUser(EmailAbstractUser):
    first_name = models.CharField(blank=True, null=True, max_length=30,)
    # middle_name = models.CharField(blank=True, null=True, max_length=30,)
    last_name = models.CharField(blank=True, null=True, max_length=30,)
    phone_number = models.CharField(max_length=15,blank=True, null=True)
    address = models.TextField(null=True)
    city = models.TextField(null=True)
    state = models.TextField(null=True)
    country = models.TextField(null=True)
    pincode = models.CharField(max_length=10)
    is_admin = models.BooleanField(default=False)
