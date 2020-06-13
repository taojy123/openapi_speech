from django.urls import path, include
from rest_framework import routers

from tapp import views

router = routers.DefaultRouter()
router.register('products', views.ProductViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

