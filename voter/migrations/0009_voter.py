# Generated by Django 4.2.1 on 2023-07-23 07:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('voter', '0008_votersignup_vard_no'),
    ]

    operations = [
        migrations.CreateModel(
            name='Voter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('age', models.IntegerField()),
                ('house_no', models.IntegerField()),
                ('aadhar_id', models.IntegerField(unique=True)),
                ('gender', models.CharField(choices=[('female', 'Female'), ('male', 'Male')], max_length=10)),
                ('image', models.ImageField(blank=True, null=True, upload_to='voter_images/')),
                ('aadhar_file', models.ImageField(blank=True, null=True, upload_to='aadhar_images/')),
                ('address', models.TextField()),
                ('city', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=100)),
                ('pin', models.CharField(max_length=10)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=15)),
            ],
        ),
    ]
