from django.urls import path
from .views import subscribe

urlpatterns = [
    path('email', subscribe, name = 'subscribe'),
]