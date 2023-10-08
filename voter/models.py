from django.db import models
from django.db.models import DateField


# Create your models here.


class VoterSignup(models.Model):
    v_name = models.CharField(max_length=100)
    aadhar_id = models.IntegerField(unique=True)
    date = models.DateField()
    phone = models.IntegerField()
    gender = models.CharField(max_length=10)
    photo = models.ImageField(upload_to='voter')
    email = models.CharField(max_length=20)
    vard_no = models.CharField(max_length=20)
    def __str__(self):
        return self.v_user

class Voter(models.Model) :
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    house_no = models.IntegerField()
    aadhar_id = models.CharField(max_length=15, unique=True)
    GENDER_CHOICES = [
        ('female', 'Female'),
        ('male', 'Male'),
        # Add more choices if needed
    ]
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    image = models.ImageField(upload_to='voter_images/')
    aadhar_file = models.ImageField(upload_to='aadhar_images/')
    address = models.TextField()
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    pin = models.CharField(max_length=10)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    confirmation = models.BooleanField(default=False)
    def __str__(self):
        return self.first_name


class Feedback(models.Model):
        name = models.CharField(max_length=100)
        email = models.EmailField()
        message = models.TextField()

        def __str__(self):
            return self.name