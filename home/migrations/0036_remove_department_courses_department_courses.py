# Generated by Django 4.2.1 on 2023-06-19 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0035_delete_timetable'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='department',
            name='courses',
        ),
        migrations.AddField(
            model_name='department',
            name='courses',
            field=models.ManyToManyField(max_length=100, to='home.subjects'),
        ),
    ]
