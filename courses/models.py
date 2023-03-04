import datetime
from django.db import models
from django.utils.text import slugify #slug yani url değerini biçimlendirme


class Category(models.Model):
    name=models.CharField(max_length=40)
    slug = models.SlugField(default="",null=False,unique=True,db_index=True,max_length=50)



    def __str__(self):
        return self.name

class Course(models.Model):
    title= models.CharField(max_length=50)
    description = models.TextField()
    imageUrl = models.CharField(max_length=50)
    date = models.DateField(default=datetime.datetime.now())
    isActive = models.BooleanField(default=False)
    isHome = models.BooleanField(default=False)
    slug = models.SlugField(default="",blank=True,editable=False,unique=True,db_index=True)##daha önce ki kayıtlar için varsayılan değer atandı ve boş geçilemez şartı koyuldu. Bu alan sonradan eklendi.
    # unique tekil alan db_index index atar. blank=True değeri form üzerindeki zorunluluğu kaldırır zaten save() metodunda title slug olarak çevildiriği için tekrar bir değer girmek gerekli değildir. girilse dahi title alanı ile güncellenmektedir.
    # editable=False form üzerinde görünmemesini sağlar.
    # category= models.ForeignKey(Category,default=2,on_delete=models.CASCADE,related_name="kurslar")
    # kurslar ile kategory arasında yabancıl anahtar oluşturuldu. models.cascade değeri ile categoryden herhangi bir kayıt silindiğinde
    #ilgili kursların silinmesi için kullanıldı. models.SET_NULL da kullanılabilir ama null değerli alabililnmesi için null=true değer yazılmalıdır.
    #aynı zamanda set_default yazılabilir default değer atanmasıyla default=null diye
    categories = models.ManyToManyField(Category)

    def save(self,*args,**kwargs):
        self.slug = slugify(self.title)
        super().save(args,kwargs)


    def __str__(self):
        return f"{self.title}"



    