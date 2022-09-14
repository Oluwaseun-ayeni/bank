# Generated by Django 4.1.1 on 2022-09-13 05:03

import bank_app.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(default='description')),
                ('account_balance', models.DecimalField(decimal_places=2, default=0.0, max_digits=20)),
                ('account_number', models.CharField(max_length=15)),
                ('account_type', models.CharField(choices=[('F', bank_app.models.FixedAccount), ('S', bank_app.models.SavingsAccount), ('C', bank_app.models.CurrentAccount)], max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.PositiveSmallIntegerField()),
                ('street', models.CharField(max_length=255)),
                ('city', models.CharField(max_length=255)),
                ('state', models.CharField(default='Lagos', max_length=255)),
                ('country', models.CharField(default='Nigeria', max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='CurrentAccount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='SavingsAccount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deposit_total', models.DecimalField(decimal_places=2, default=0.0, max_digits=20)),
                ('deposit_bank', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('mobile', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=254)),
                ('username', models.CharField(max_length=255)),
                ('user', models.CharField(choices=[('C', 'Customer'), ('E', 'Employee')], max_length=1)),
                ('address', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='bank_app.address')),
            ],
        ),
        migrations.CreateModel(
            name='FixedAccount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deposit_amount', models.DecimalField(decimal_places=2, default=0.0, max_digits=20)),
                ('deposit_bank', models.CharField(max_length=255)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bank_app.account')),
            ],
        ),
        migrations.AddField(
            model_name='account',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='bank_app.user'),
        ),
    ]
