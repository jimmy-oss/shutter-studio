from django.shortcuts import render
from .models  import Category, Photo

# Create your views here.
def gallery (request):
       category = Category.objects.all()
       photos = Photo.objects.all()
       context = {'categories':category,'photos':photos}
       return render(request,'photos/gallery.html',context)
     
def viewPhoto (request, pk):
       photo = Photo.objects.get(id=pk)
       return render(request,'photos/photo.html',{'photo':photo})
  
def addPhoto (request):
       category = Category.objects.all()
       context = {'categories':category}
       return render(request,'photos/add.html',context)
