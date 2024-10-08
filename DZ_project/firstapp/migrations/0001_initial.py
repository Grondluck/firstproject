# Generated by Django 5.1.1 on 2024-09-27 23:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='clients',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Имя')),
                ('nickname', models.CharField(max_length=100, verbose_name='Никнейм')),
                ('lastname', models.CharField(default=None, max_length=100, verbose_name='Фамилия')),
                ('balance', models.FloatField(default=0, verbose_name='Баланс')),
                ('dor', models.DateField(auto_now=True, verbose_name='Дата регистрации')),
            ],
        ),
    ]
