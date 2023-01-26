from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager,PermissionsMixin

from django.db.models.deletion import CASCADE
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
import random

class MyAccountManager(BaseUserManager):
    """defines the methods to manage the custom user to be created
    Args:
        BaseUserManager ([type]): [description]
    Returns:
        [type]: [description]
    """
    def create_user(self,phone_number,password=None):
        if not phone_number:
            raise ValueError("Users must have a phone number")
        
        user = self.model(
            phone_number = phone_number,
            password = password
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self,phone_number,password):
        user = self.create_user(
            phone_number = phone_number,
            password = password,
        )

        user.is_admin = True
        user.is_superuser = True
        user.is_staff = True

        user.save(using=self._db)
        return user

class Account(AbstractBaseUser,PermissionsMixin):
    """This will define the custom user model to be used
    Args:
        AbstractBaseUser ([type]): [description]
    """
    id = models.AutoField(primary_key=True),
    phone_number = models.CharField(
        verbose_name="phone number",
        max_length=15,
        null=True,
        unique=True
        )
    date_joined = models.DateTimeField(
        verbose_name="date joined"
        ,auto_now_add=True
        )
    last_login = models.DateTimeField(
        verbose_name="last login",
        auto_now=True
        )
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = MyAccountManager()

    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.phone_number

    def has_perm(self,perm,obj=None):
        return self.is_admin

    def has_module_perms(self,app_label):
        return True

    def delete_user(self):
        self.delete()

from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)

class Code(models.Model):
    verification_code = models.CharField(max_length=5,
    verbose_name="code",
    unique=True,
    )
    user = models.OneToOneField(Account,
    on_delete=CASCADE,
    blank=True, 
    null=True, 
    unique=True,
    default="",
    related_name="profile")

    def __str__(self):
        return self.verification_code

    def save(self,code_items=None,*args,**kwargs):
        number_list = [x for x in range(10)]
        code_items = []

        for i in range(5):
            num = random.choice(number_list)
            code_items.append(num)
        code_to_string = "".join(str(item) for item in code_items)
        self.verification_code = code_to_string
        super().save(*args,**kwargs)
        return self.verification_code

class Username(models.Model):
    username = models.CharField(max_length=1000)
    code = models.OneToOneField(Code, on_delete=CASCADE)

    def __str__(self):
        return self.username
    





