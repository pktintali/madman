from django.db import router
from django.urls import path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register('categories',views.CategoryViewSet,basename='categories')

urlpatterns = router.urls
