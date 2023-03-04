from django.contrib import admin
from .models import Course,Category
# Register your models here.



@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ("title","isActive","slug","description","category_list")
    list_display_links=("title","slug")
    readonly_fields = ("slug",)
    list_filter = ("title","isActive")
    list_editable = ("isActive",)
    search_fields = ("title","description")


    def category_list(self,obj):
        html=""
        for category in obj.categories.all():
            html+=category.name+','
        
        return html

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name","slug","course_count")
    prepopulated_fields={"slug":("name",),}


    def course_count(self,obj):
        return obj.course_set.count()


# admin.site.register(Course)
# #django admin modülü içerisinde course modelini ekler oradan dinamik formlardan CRUD işlemlerini yapmamızı sağlar.
# admin.site.register(Category)

