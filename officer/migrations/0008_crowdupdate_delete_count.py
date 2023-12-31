# Generated by Django 4.2.1 on 2023-06-24 07:33

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('officer', '0007_count'),
    ]

    operations = [
        migrations.CreateModel(
            name='CrowdUpdate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('booth_no', models.CharField(max_length=50)),
                ('count', models.PositiveIntegerField()),
                ('percentage', models.IntegerField()),
                ('timestamp', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.DeleteModel(
            name='Count',
        ),
    ]
