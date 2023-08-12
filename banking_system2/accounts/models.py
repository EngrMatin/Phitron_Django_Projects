from decimal import Decimal
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.validators import (MinValueValidator, MaxValueValidator)
from .managers import UserManager
from .constants import GENDER_CHOICE

# Create your models here.
class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, null=False, blank=False)
    objects = UserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    def __str__(self):
        return self.email
    
    @property
    def balance(self):
        if hasattr(self, 'account'):
            return self.account.balance
        return 0

class BankAccountType(models.Model):
    name = models.CharField(max_length=128)
    max_withdrawal_limit = models.DecimalField(max_digits=12, decimal_places=2)
    def __str__(self):
        return self.name

class UserBankAccount(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='account')
    account_type = models.ForeignKey(BankAccountType, on_delete=models.CASCADE, related_name='accounts')
    account_no = models.PositiveIntegerField(unique=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICE )
    birth_date = models.DateField(null=True, blank=True)
    balance = models.DecimalField(default=0, max_digits=12, decimal_places=2)
    initial_deposit_date = models.DateField(auto_now_add=True)
    # initial_deposit_date = models.DateField(null=True, blank=True)
    def __str__(self):
        return str(self.account_no)
    
class UserAddress(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='address')
    street_address = models.CharField(max_length=512)
    city = models.CharField(max_length=256)
    postal_code = models.PositiveIntegerField()
    country = models.CharField(max_length=128)
    def __str__(self):
        return self.user.email
    
