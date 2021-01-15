from django.urls import path
from . import views

urlpatterns = [
    path('<slug:category>', views.category, name= 'category'),
]