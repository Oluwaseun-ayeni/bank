from django.db import models

# Create your models here.

class Customer(models.Model):
    address1 = models.CharField(max_length=30)
    address2 = models.CharField(max_length=30)
    first_name = models.CharField(max_length=30)
    middle_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    city = models.CharField(max_length=20)
    state = models.CharField(max_length=30, default='Lagos')
    zip_code = models.IntegerField(max_length=8)
    email_address = models.EmailField()
    home_phone = models.CharField(max_length=15,default=null)
    cell_phone = models.CharField(max_length=15)
    work_phone = models.CharField(max_length=15,default=null)

class Account(models.Model):
    current_balance = models.DecimalField()
    account_status_type = models.OneToOneField("AccountStatusType", default=null)
    customer = models.ManyToManyField(Customer)
    account_type = models.OneToOneField('AccountType',on_delete=models.PROTECT)
    interest_savings_rate = models.OneToOneField('SavingsInterestRates', on_delete=models.PROTECT)

class AccountStatusType(models.Model):
    account_status_description = models.TextField()

class AccountType(models.Model):
    account_type_description = models.TextField()


class Employee(models.Model):
    first_name = models.CharField(max_length=255)
    middle_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    is_manager = models.BooleanField()

class OverDraftLog(models.Model):
    account = models.ForeignKey(Account, primary_key=True)
    over_draft_date = models.DateTimeField(auto_now=True)
    over_draft_transaction_description = models.TextField()

class TransactionType(models.Model):
    transcation_type_name = models.CharField(max_length=10)
    transcation_type_description = models.TextField()
    transcation_fee_amount = models.DecimalField(max_digits=10, decimal_places=2)

class TranscationLog(models.Model):
    transaction_date = models.DateTimeField(auto_now=True)
    transaction_type = models.OneToOneField('TransactionType', on_delete=models.PROTECT)
    transaction_amount = models.DecimalField(max_digits=20, decimal_places=2)
    new_Balance = models.DecimalField(max_digits=20, decimal_places=2)
    account = models.ForeignKey('Account',on_delete=models.SET_NULL,null=True)
    customer = models.ForeignKey('Customer',on_delete=models.SET_NULL,null=True)
    employee = models.ForeignKey('Employee',on_delete=models.SET_NULL,null=True)
    user_login = models.ForeignKey('UserLogin',on_delete=models.SET_NULL,null=True)

class SavingsInterestRates(models.Model):
    interest_rate_value = models.DecimalField(max_digits=20, decimal_places=2)
    interest_rate_description = models.TextField()
