from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('404', views.error_handler, name='error_handler'),
]