# Generated by Django 4.2.5 on 2024-03-19 14:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_customuser_profileimage'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='profileImage',
        ),
    ]
