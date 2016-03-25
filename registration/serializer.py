from rest_framework import serializers
from django.contrib.auth import get_user_model
from    .models import Company



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        exclude = ('password','id')

class CompanySerializer(serializers.ModelSerializer):
    users = serializers.StringRelatedField(many=True)

    class Meta:
        model = Company
