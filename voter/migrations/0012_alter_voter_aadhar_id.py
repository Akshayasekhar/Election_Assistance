# Generated by Django 4.2.1 on 2023-07-25 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('voter', '0011_alter_voter_aadhar_file_alter_voter_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='voter',
            name='aadhar_id',
            field=models.CharField(max_length=15, unique=True),
        ),
    ]
