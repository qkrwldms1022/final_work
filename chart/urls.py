from django.urls import path
from . import views

urlpatterns = [
    path('covie19new', views.home, name='home'),
]