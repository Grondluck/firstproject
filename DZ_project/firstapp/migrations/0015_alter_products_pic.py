# Generated by Django 4.2.3 on 2024-09-30 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0014_products_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='pic',
            field=models.ImageField(blank=True, upload_to='firstapp/static/img'),
        ),
    ]
