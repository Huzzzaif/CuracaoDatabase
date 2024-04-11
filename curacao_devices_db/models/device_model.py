from django.db import models

class Device(models.Model):
    STATUS_CHOICES = [
        ("A", "Active"), 
        ("I", "Inactive"), 
        ("B", "Broken"), 
        ("R", "Repairing"), 
        ("D", "Destroyed")
    ]
    serial = models.CharField(max_length=100, primary_key=True) 
    MAC = models.CharField(max_length=100)
    cid = models.IntegerField()
    mid = models.IntegerField()
    tid = models.IntegerField()
    store = models.CharField(max_length=100)
    location = models.ForeignKey("Location", on_delete=models.PROTECT)
    department = models.ForeignKey("Department", on_delete=models.PROTECT)
    pstation = models.CharField(max_length=100)
    register = models.CharField(max_length=100)
    ip = models.CharField(max_length=100)
    labelid = models.CharField(max_length=100)
    itassetid = models.IntegerField()
    notes = models.CharField(max_length=100)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default="A")
    statusnotes = models.CharField(max_length=100)
  
    def __str__(self): 
        return self.serial