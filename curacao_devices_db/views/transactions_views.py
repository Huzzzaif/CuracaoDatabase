from rest_framework import generics
from curacao_devices_db.models import Transaction
from curacao_devices_db.serializer import TransactionsSerializer
class TransactionsView(generics.ListCreateAPIView):
    serializer_class = TransactionsSerializer
    queryset = Transaction.objects.all()