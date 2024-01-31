from django.db import models
from datetime import date
# Create your models here.
class Properties(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    types_list = [
        ('apartment', 'Apartment'),
        ('villa', 'Villa'),
        ('home', 'Home'),
        ('office', 'Office'),
        ('building', 'Building'),
        ('townhose', 'Townhouse'),
        ('shop', 'Shop'),
        ('garage', 'Garage'),
        ]
    property_type = models.CharField(max_length=50, choices=types_list)
    status_list = [('featured', 'Featured'), ('on_sale', 'On Sale'), ('on_rent', 'On Rent')]
    property_status = models.CharField(max_length=50, choices=status_list)
    location = models.CharField(max_length=100)
    bedrooms = models.IntegerField()
    bathrooms = models.IntegerField()
    floors = models.IntegerField()
    garages = models.IntegerField()
    area = models.FloatField()
    price= models.FloatField()
    map_link = models.CharField(max_length = 500)
    address= models.CharField(max_length = 500)
    image = models.ImageField(upload_to='property_img')

    def __str__(self):
        return self.title
    

class Contact(models.Model):
    name= models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    subject = models.CharField(max_length=200)
    message= models.TextField()
    date = models.DateField(default=date.today())

    def __str__(self):
        return f"Message from {self.name} on {self.date}"


