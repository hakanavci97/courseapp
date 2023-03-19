
from django.urls import path
from . import views




urlpatterns = [

     path('',views.index, name="index"),
     path('search',views.search,name="search"),
     path('create-course',views.create_course,name="create_course"),
     path('course-list',views.course_list,name="course_list"),
     path('course-edit/<int:id>',views.course_edit,name="course_edit"),
     path('<kurs_id>',views.details,name="course_details"),
     path('kategori/<slug:slug>',views.getCoursesByCategory, name="courseByCategory"),
    

     # path('<int:categoryId>',views.getCoursesByCategoryId),
     # path('<category>',views.getCoursesByCategory)



]
