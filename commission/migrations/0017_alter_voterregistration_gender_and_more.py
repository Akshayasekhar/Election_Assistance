# Generated by Django 4.2.1 on 2023-07-26 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('commission', '0016_alter_voterregistration_aadhar_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='voterregistration',
            name='gender',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='voterregistration',
            name='voter_id',
            field=models.CharField(max_length=12, unique=True),
        ),
    ]
