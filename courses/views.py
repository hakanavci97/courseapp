from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpResponseNotFound
from django.urls import reverse
# Create your views here.

data={
    "django":"django web framework eğitimi",
    "mobil":"mobil geliştirme eğitimi",
    "web":"web geliştirme eğitimi",

}



def index(request):
    category_list=list(data.keys())

    return render(request,'courses/index.html',{
        'categories':category_list
    })


def getCoursesByCategory(request, category):
    return HttpResponse(f"{category} Dinamik Url Tanımlama")


def getCoursesByCategoryName(request, categoryName):
    try:
        categoryText=data[categoryName]
        return render(request, 'courses/courses.html',{
            'category':categoryName,
            'category_text':categoryText
        })
    except:
        return HttpResponseNotFound("yanlış bir değer girdiniz")

def  getCoursesByCategoryId(request, categoryId):
    categoryList= list(data.keys())
    if(categoryId>len(categoryList)):
        return HttpResponseNotFound("Yanlış değer girdiniz")

    categoryName=categoryList[categoryId-1]

    redirectUrl=reverse('courseByCategory',args=[categoryName])

    return redirect(redirectUrl)
