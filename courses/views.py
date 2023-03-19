from datetime import date,datetime
from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpResponseNotFound
from django.urls import reverse

from courses.forms import CourseCreateForm
from .models import Category,Course
from django.core.paginator import Paginator ## sayfalama için kullanılan kütüphane



# Create your views here.

db={
       "courses":[
        {
            "title":"Javascript Kursu",
            "description":"Javascript kurs açıklaması",
            "imageUrl":"1.jpg",
            "slug":"javascript-kursu",
            "date":datetime.now(),
            "isActive":True,
            "isUpdated":True
            
        },
        {
            "title":"python Kursu",
            "description":"python kurs açıklaması",
            "imageUrl":"2.jpg",
            "slug":"python-kursu",
            "date":date(2022,10,10),
            "isActive":True,
            "isUpdated":True
            
        },
        {
            "title":"web geliştirme Kursu",
            "description":"web geliştirme kurs açıklaması",
            "imageUrl":"3.jpg",
            "slug":"web-geliştirme-kursu",
            "date":date(2022,10,10),
            "isActive":True,
            "isUpdated":False

            
        }
       ],
       "categories": [
        { "id":1,"name":"programalama","slug":"programlama"},
        {"id":2,"name":"web geliştirme","slug":"web-gelistirme"},
        {"id":3,"name":"mobil uygulama","slug":"mobil-uygulama"}]
}



def index(request):
    # kurslar = db["courses"]
    #list comphension dict sözlük içerisinde belirli alana göre filtreleme yapma
    #index.html kısmında if blokları ile yapılabileceği gibi aşağıdaki örnekteki gibi de yapılabilir
    # kurslar = [course for course in db["courses"] if course["isActive"]==True]
    kurslar = Course.objects.all()

    
    kategoriler=Category.objects.all()

    #3 farklı şekilde burada olduğu gibi yine filtreleme yapılabilir.
    # for kurs in db["courses"]:
    #     if kurs["isActive"]==True:
    #         kurslar.append(kurs)

    if request.path.__contains__('/kurslar/'):
        print(True) 
    print(request.path)
    return render(request,'courses/index.html',{
        'categories':kategoriler,
        'courses':kurslar
    })


def details(request,kurs_id):
    course = Course.objects.get(pk=kurs_id)
    content = {
        'course':course
    }
    return render(request, "courses/details.html",content)



# def getCoursesByCategory(request, category):
#     return HttpResponse(f"{category} Dinamik Url Tanımlama")


def getCoursesByCategory(request, slug):
    kurslar = Course.objects.filter(categories__slug=slug, isActive=True)
    kategoriler= Category.objects.all()

    paginator = Paginator(kurslar,2)
    page=request.GET.get('page',1)
    page_obj = paginator.page(page)






    return render(request,"courses/partials/_pagination.html",{
        'categories':kategoriler,
        'page_obj':page_obj,
        'seciliKategori':slug
    })
    
    
    
    # try:
    #     categoryText=Category.objects.get(name=categoryName)
   
    #     return render(request, 'courses/courses.html',{
    #         'category':categoryName,
    #         'category_text':categoryText
    #     })
    # except:
    #     return HttpResponseNotFound("yanlış bir değer girdiniz")

# def  getCoursesByCategoryId(request, categoryId):
#     categoryList= list(data.keys())
#     if(categoryId>len(categoryList)):
#         return HttpResponseNotFound("Yanlış değer girdiniz")

#     categoryName=categoryList[categoryId-1]

#     redirectUrl=reverse('courseByCategory',args=[categoryName])

#     return redirect(redirectUrl)


def search(request):
    if "q" in request.GET and request.GET["q"] != "":
        q = request.GET["q"]
        kurslar = Course.objects.filter(isActive=True, title__contains=q).order_by("date")
        kategoriler=Category.objects.all()
    else:
        return redirect("/kurslar")
    
    

    return render(request,'courses/search.html',{
            'categories':kategoriler,
            'courses':kurslar,
    })

def course_list(request):
    kurslar = Course.objects.all()
    return render(request,'courses/course-list.html',{
        'courses':kurslar
    })

def course_edit(request, id):
    pass

def create_course(request):
    if request.method == "POST":

        form = CourseCreateForm(request.POST)

        if form.is_valid():
            form.save()
            # kurs = Course(
            #     title = form.cleaned_data["title"],
            #     description = form.cleaned_data["description"],
            #     imageUrl =  form.cleaned_data["imageUrl"],
            #     slug = form.cleaned_data["slug"],
            # )
            # kurs.save()

            return redirect("/kurslar")




        # title =request.POST["title"]
        # description = request.POST["description"]
        # imageUrl = request.POST["imageUrl"]
        # date = request.POST["date"]
        # slug = request.POST["slug"]
        # isActive = request.POST.get("isActive", False)
        # isHome = request.POST.get("isHome",False) # checkedbox değeri post metodun işaretlenmediği zaman değer döndürmez ve hata verir hata vermesinde diye default değer false gönderme işlemi yapıldı.


        # if isActive == "on":
        #     isActive=True
        # if isHome == "on":
        #     isHome=True

        # kurs = Course(title=title,description=description,imageUrl=imageUrl,date=date,slug=slug,isActive=isActive,isHome=isHome)
        # kurs.save()
        # return redirect("/kurslar")
    else:
        form = CourseCreateForm()
    return render(request, "courses/create-course.html", {"form":form,"kategori":1})