from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.utils.timezone import now
from .models import Device, Transaction
import json
from .serializer import DeviceSerializer

@receiver(post_save, sender=Device)
def create_update_device_history(sender, instance, created, **kwargs):
    transaction_type = "insert" if created else "update"

    Transaction.objects.create(
        time= now().strftime("%Y-%m-%d %H:%M:%S"),  # Format time as a string
        user= "username",  # You need to get the actual user from the request or context
        geolocation="geolocation_info",  # Add actual geolocation information
        type=transaction_type,
        serial=instance,  # This is the ForeignKey link to the Device instance
        MAC=instance.MAC,
        cid=instance.cid,
        tid=instance.tid,
        mid=instance.mid,
        store=instance.store,
        location=instance.location,
        department=instance.department,
        pstation=instance.pstation,
        register=instance.register,
        ip=instance.ip,
        labelid=instance.labelid,
        itassetid=instance.itassetid,
        notes=instance.notes,  # Add any notes if needed
        status=instance.status,
        statusnotes=instance.statusnotes  # Add status notes if applicable
    )
    


