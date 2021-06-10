# Generated by Django 2.2.13 on 2021-06-10 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Accept',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=200)),
                ('requested_money', models.IntegerField(blank=True, null=True)),
                ('precentage', models.IntegerField()),
                ('payed_money', models.IntegerField(blank=True, null=True)),
                ('borrower_name', models.CharField(blank=True, max_length=200, null=True)),
                ('lending_time', models.IntegerField(blank=True, null=True)),
                ('loan_status', models.CharField(blank=True, max_length=200, null=True)),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='date published')),
                ('pay_date', models.DateTimeField(blank=True, null=True, verbose_name='date published')),
            ],
        ),
        migrations.CreateModel(
            name='Loan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=200)),
                ('requested_money', models.IntegerField()),
                ('payed_money', models.IntegerField(blank=True, null=True)),
                ('loaner_name', models.CharField(blank=True, max_length=200, null=True)),
                ('lending_time', models.IntegerField()),
                ('loan_status', models.CharField(blank=True, max_length=200, null=True)),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='date published')),
                ('pay_date', models.DateTimeField(blank=True, null=True, verbose_name='date published')),
            ],
        ),
    ]