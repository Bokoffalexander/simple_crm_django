from django.db import models

# Create your models here.

class Record(models.Model):

    first_name = models.CharField(max_length=99)
    last_name = models.CharField(max_length=99)
    phone = models.CharField(max_length=12)
    email = models.CharField(max_length=99)
    
    date_added = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
    
        return (f"{self.first_name} {self.last_name}")