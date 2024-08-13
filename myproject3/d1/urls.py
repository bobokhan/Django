from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),  # This maps the root URL to the index view
    path('counter',views.counter),
]
