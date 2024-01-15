from django.db import models

# Create your models here.
class Musician(models.Model):
        first_name = models.CharField(max_length=25)
        last_name = models.CharField(max_length=25)
        email = models.EmailField()
        phone_no = models.CharField(max_length=12)
        instrument_type= models.CharField(max_length=50)

        def __str__(self):
                return self.first_name