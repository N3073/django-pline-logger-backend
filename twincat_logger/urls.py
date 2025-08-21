from django.urls import path
from . import views

urlpatterns = [
    path('tc_log/<str:plineid>', views.tc_log, name='Twincat Logger'),
]
