from django.db import models

# Create your models here.


class countofficer(models.Model):
    booth_no = models.IntegerField()
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    gender = models.CharField(max_length=14)
    phone = models.IntegerField()
    email = models.CharField(max_length=40)
    username = models.CharField(max_length=40, unique=True)
    password = models.CharField(max_length=40)


from django.utils import timezone

class CrowdUpdate(models.Model):
    booth_no = models.CharField(max_length=50)
    count = models.PositiveIntegerField()
    percentage = models.IntegerField()
    timestamp = models.DateTimeField(default=timezone.now)

    # def __str__(self):
    #     return f'{self.booth_no} - {self.count}'
