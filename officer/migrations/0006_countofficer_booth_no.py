# Generated by Django 4.2.1 on 2023-06-15 07:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('officer', '0005_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='countofficer',
            name='booth_no',
            field=models.IntegerField(default=15.865079365079366),
            preserve_default=False,
        ),
    ]
