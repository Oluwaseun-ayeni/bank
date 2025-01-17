# Generated by Django 4.1 on 2022-09-14 21:22

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
                ('current_balance', models.DecimalField(decimal_places=2, max_digits=20)),
                ('account_type', models.CharField(choices=[('S', 'savings'), ('C', 'current'), ('F', 'fixed')], max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='AccountStatusType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account_status_description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address1', models.CharField(max_length=30)),
                ('address2', models.CharField(max_length=30)),
                ('first_name', models.CharField(max_length=30)),
                ('middle_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('city', models.CharField(max_length=20)),
                ('state', models.CharField(default='Lagos', max_length=30)),
                ('zip_code', models.IntegerField()),
                ('email_address', models.EmailField(max_length=254)),
                ('home_phone', models.CharField(max_length=15, null=True)),
                ('cell_phone', models.CharField(max_length=15)),
                ('work_phone', models.CharField(max_length=15, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255)),
                ('middle_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('is_manager', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='SavingsInterestRates',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('interest_rate_value', models.DecimalField(decimal_places=2, max_digits=20)),
                ('interest_rate_description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='TranscationLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transaction_date', models.DateTimeField(auto_now=True)),
                ('transaction_type', models.CharField(choices=[('S', 'savings'), ('C', 'current'), ('F', 'fixed')], max_length=1)),
                ('transaction_amount', models.DecimalField(decimal_places=2, max_digits=20)),
                ('new_Balance', models.DecimalField(decimal_places=2, max_digits=20)),
                ('account', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='bank_app.account')),
                ('customer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='bank_app.customer')),
                ('employee', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='bank_app.employee')),
            ],
        ),
        migrations.CreateModel(
            name='OverDraftLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('over_draft_date', models.DateTimeField(auto_now=True)),
                ('over_draft_transaction_description', models.TextField()),
                ('account', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='bank_app.account')),
            ],
        ),
        migrations.AddField(
            model_name='account',
            name='account_status_type',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='bank_app.accountstatustype'),
        ),
        migrations.AddField(
            model_name='account',
            name='customer',
            field=models.ManyToManyField(to='bank_app.customer'),
        ),
        migrations.AddField(
            model_name='account',
            name='interest_savings_rate',
            field=models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='bank_app.savingsinterestrates'),
        ),
    ]
