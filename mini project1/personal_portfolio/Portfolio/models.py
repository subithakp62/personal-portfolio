from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=300)
    email = models.EmailField(max_length=300)
    phone = models.CharField(max_length=300)
    concern = models.TextField(max_length=30)
   

    
    def ___str__(self):
        return self.name
    
