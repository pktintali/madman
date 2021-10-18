from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.viewsets import ModelViewSet
from myapp.models import Category
from .serializers import CtegorySerializer

# Create your views here.
def welcome(request):
    return HttpResponse('Welcome to myapp')

class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CtegorySerializer