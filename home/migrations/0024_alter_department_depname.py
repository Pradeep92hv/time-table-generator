# Generated by Django 4.2.1 on 2023-06-17 19:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0023_department'),
    ]

    operations = [
        migrations.AlterField(
            model_name='department',
            name='depname',
            field=models.CharField(default='2', max_length=30),
        ),
    ]
