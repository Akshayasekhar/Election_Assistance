# Generated by Django 4.2.1 on 2023-07-14 12:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('commission', '0007_alter_officeradd_username'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='person',
            name='no',
        ),
    ]
