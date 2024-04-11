from django.db import models

class Location(models.Model): 
    #location_id = models.CharField(max_length = 30) 
    name = models.CharField(max_length = 30) 
    status = models.CharField(max_length = 1) 
  
    def __str__(self): 
        return self.name 