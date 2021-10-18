from rest_framework import serializers
from .models import Category

class CtegorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id','title']