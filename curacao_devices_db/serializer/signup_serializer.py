from rest_framework import serializers
from curacao_devices_db.models import User

class SignupSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'