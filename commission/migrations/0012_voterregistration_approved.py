# Generated by Django 4.2.1 on 2023-07-20 07:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('commission', '0011_voterregistration'),
    ]

    operations = [
        migrations.AddField(
            model_name='voterregistration',
            name='approved',
            field=models.BooleanField(default=False),
        ),
    ]