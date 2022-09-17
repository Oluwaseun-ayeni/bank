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
    zip_code = models.CharField(max_length=6)
    email_address = models.EmailField(unique=True)
    password = models.CharField(max_length=255,default='')
    home_phone = models.CharField(max_length=15, null=True)
    cell_phone = models.CharField(max_length=15)
    work_phone = models.CharField(max_length=15, null=True)

    def __str__(self):
        return '%s %s %s %s ' % (self.first_name, self.last_name, self.cell_phone, self.email_address)

class Account(models.Model):
    ACCOUNT_CHOICES = (
        ('S', 'savings'),
        ('C', "current"),
        ('F', 'fixed')
    )
    current_balance = models.DecimalField(max_digits=20, decimal_places=2)
    account_status_type = models.OneToOneField("AccountStatusType", on_delete=models.SET_NULL, null=True)
    customer = models.ForeignKey('Customer', on_delete=models.CASCADE,null=True)
    account_type = models.CharField(max_length=1, choices=ACCOUNT_CHOICES)
    interest_savings_rate = models.OneToOneField('SavingsInterestRates', on_delete=models.PROTECT)


class AccountStatusType(models.Model):
    account_status_description = models.TextField()


class Employee(models.Model):
    first_name = models.CharField(max_length=255)
    middle_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    is_manager = models.BooleanField()
    email_address = models.EmailField(unique=True,default='')
    password = models.CharField(max_length=255,default='')
    home_phone = models.CharField(max_length=15, null=True)
    cell_phone = models.CharField(max_length=15,default='')
    work_phone = models.CharField(max_length=15, null=True)


class OverDraftLog(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    over_draft_date = models.DateTimeField(auto_now=True)
    over_draft_transaction_description = models.TextField()


class TranscationLog(models.Model):
    TRANCTION_CHOICES = (
        ('S', 'savings'),
        ('C', "current"),
        ('F', 'fixed')
    )
    transaction_date = models.DateTimeField(auto_now=True)
    transaction_type = models.CharField(max_length=1, choices=TRANCTION_CHOICES)
    transaction_amount = models.DecimalField(max_digits=20, decimal_places=2)
    transaction_fee_amount = models.DecimalField(max_digits=20, decimal_places=2, null=True)
    new_Balance = models.DecimalField(max_digits=20, decimal_places=2)
    account = models.ForeignKey('Account', on_delete=models.CASCADE,null=True)
    customer = models.ForeignKey('Customer', on_delete=models.CASCADE,null=True)
    employee = models.ForeignKey('Employee', on_delete=models.CASCADE,null=True)


class SavingsInterestRates(models.Model):
    interest_rate_value = models.DecimalField(max_digits=20, decimal_places=2)
    interest_rate_description = models.TextField()
