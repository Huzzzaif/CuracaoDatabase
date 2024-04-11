from rest_framework import generics

from curacao_devices_db.models import Department
from curacao_devices_db.serializer import DepartmentSerializer


class DepartmentsView(generics.ListCreateAPIView):
    serializer_class = DepartmentSerializer
    queryset = Department.objects.all()