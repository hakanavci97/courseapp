
from django.urls import path
from . import views



urlpatterns = [

     path('',views.home),
     path('hakkimizda',views.hakkimizda)

]
