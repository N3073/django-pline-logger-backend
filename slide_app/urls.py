from django.urls import path
from . import views

urlpatterns = [
    path('slide_app', views.slide_home, name='Slides'),
    path('slide_app/<str:slide_id>', views.slide_page, name='Slide view'),
    
]