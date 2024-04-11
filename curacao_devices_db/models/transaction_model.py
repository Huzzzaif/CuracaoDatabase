from django.db import models

class Transaction(models.Model):
    STATUS_CHOICES = [
        ("A", "Active"), 
        ("I", "Inactive"), 
        ("B", "Broken"), 
        ("R", "Repairing"), 
        ("D", "Destroyed")
    ]
    time = models.CharField(max_length=100) 
    user = models.CharField(max_length=100) 
    geolocation = models.CharField(max_length=100) 
    type = models.CharField(max_length=100) 
    serial = models.ForeignKey('Device', on_delete=models.CASCADE)
    MAC = models.CharField(max_length=100) 
    cid = models.CharField(max_length=100) 
    tid = models.CharField(max_length=100) 
    mid = models.CharField(max_length=100) 
    store = models.CharField(max_length=100) 
    location = models.CharField(max_length=100) 
    department = models.CharField(max_length=100) 
    pstation = models.CharField(max_length=100) 
    register = models.CharField(max_length=100) 
    ip = models.CharField(max_length=100) 
    labelid = models.CharField(max_length=100) 
    itassetid = models.IntegerField() 
    notes = models.CharField(max_length=100) 
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default="A")
    statusnotes = models.CharField(max_length=100)
    def __str__(self): 
        return str(self.serial) + " " + self.time 