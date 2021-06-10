from rest_framework import viewsets
from .serializers import userSerializers
from django.contrib.auth.models import Loan


class userviewsets(viewsets.ModelViewSet):
    queryset = Loan.objects.all()
    serializer_class = userSerializers
