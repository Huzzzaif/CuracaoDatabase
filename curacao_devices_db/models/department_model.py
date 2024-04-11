from django.db import models

class Department(models.Model): 
    department = models.CharField(max_length = 30, primary_key = True)  
    status = models.CharField(max_length = 1) 
  
    def __str__(self): 
        return self.department 


    



