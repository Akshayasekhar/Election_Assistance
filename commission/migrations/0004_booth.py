# Generated by Django 4.2.1 on 2023-06-15 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('commission', '0003_officeradd_booth_no_person_booth_no'),
    ]

    operations = [
        migrations.CreateModel(
            name='Booth',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('booth_no', models.IntegerField()),
                ('location', models.CharField(max_length=100)),
            ],
        ),
    ]