# Generated by Django 4.2.1 on 2023-06-17 10:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('voter', '0007_votersignup_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='votersignup',
            name='vard_no',
            field=models.CharField(default=47.595238095238095, max_length=20),
            preserve_default=False,
        ),
    ]
