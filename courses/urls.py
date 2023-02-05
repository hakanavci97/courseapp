
from django.urls import path
from . import views




urlpatterns = [

     path('',views.index),
     path('<int:categoryId>',views.getCoursesByCategoryId),
     path('<str:categoryName>',views.getCoursesByCategoryName, name="courseByCategory"),
     path('<category>',views.getCoursesByCategory)



]
