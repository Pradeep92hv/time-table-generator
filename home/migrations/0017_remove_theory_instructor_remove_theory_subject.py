# Generated by Django 4.2.1 on 2023-06-16 13:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0016_theory_instructor_theory_subject'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='theory',
            name='instructor',
        ),
        migrations.RemoveField(
            model_name='theory',
            name='subject',
        ),
    ]
