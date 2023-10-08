from django.db import models
from django.db.models import DateField
from voter.models import VoterSignup


# Create your models here.


class OfficerAdd(models.Model):
    fname = models.CharField(max_length=50)
    sname = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    radio = models.CharField(max_length=14)
    phone = models.IntegerField()
    booth_no = models.IntegerField()
    email = models.CharField(max_length=25)
    username = models.CharField(max_length=10, unique=True)
    password = models.CharField(max_length=10)

    def __str__(self):
       return self.username



# models.py

class Person(models.Model):
    voter_id = models.CharField(max_length=14, unique=True)
    name = models.CharField(max_length=100)
    aadhar_id = models.CharField(max_length=14, unique=True)
    house_no = models.CharField(max_length=100)
    age = models.IntegerField()
    gender = models.CharField(max_length=20)
    image = models.ImageField(upload_to='admin')
    booth_no = models.IntegerField()
    verified = models.BooleanField(default=False)  # New field for verification status


class VoterRegistration(models.Model):
    voter_id = models.CharField(max_length=12, unique=True)
    name = models.CharField(max_length=100)
    aadhar_id = models.CharField(max_length=14, unique=True)
    house_no = models.CharField(max_length=20)
    age = models.PositiveIntegerField()
    gender = models.CharField(max_length=10)
    image = models.ImageField(upload_to='voter_images/')
    action = models.BooleanField(default=False)


class Booth(models.Model):
    booth_no = models.IntegerField(unique=True)
    location = models.CharField(max_length=100)


class Result(models.Model):
    constituency = models.CharField(max_length=20,unique=True)
    c_name = models.CharField(max_length=20)
    party_name = models.CharField(max_length=20)
    vote_count = models.IntegerField()
    percentage = models.CharField(max_length=10)
    photo = models.ImageField(upload_to='commission')

