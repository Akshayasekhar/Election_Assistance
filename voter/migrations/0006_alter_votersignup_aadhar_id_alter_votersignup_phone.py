# Generated by Django 4.2.1 on 2023-06-05 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('voter', '0005_remove_votersignup_password_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='votersignup',
            name='aadhar_id',
            field=models.IntegerField(unique=True),
        ),
        migrations.AlterField(
            model_name='votersignup',
            name='phone',
            field=models.IntegerField(),
        ),
    ]
