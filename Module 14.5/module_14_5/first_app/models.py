from django.db import models

# Create your models here.

class MyModel(models.Model):
        name = models.CharField(max_length=20)
        roll = models.AutoField(primary_key=True)
        address = models.TextField()
        boolean_field = models.BooleanField(default=True)
        
        def __str__(self):
                return  f"Roll: {self.roll} - Name: {self.name}"