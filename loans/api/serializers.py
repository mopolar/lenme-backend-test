from rest_framework import serializers
from django.contrib.auth.models import Loan


class userSerializers(serializers.ModelSerializer):

    class Meta:
        model = Loan
        fields =  '__all__'
