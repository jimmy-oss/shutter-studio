from django.db import models
from cloudinary.models import CloudinaryField

 

 

# Create your models here.
class Category (models.Model):
     name = models.CharField(max_length=100, null=False,blank=False)
     
def save_gallery(self):
        '''
        Method to save the gallery to the database.
        '''
        self.save()

def delete_gallery(self):
        '''
        Method to delete the gallery from the database.
        '''
        self.delete()
@classmethod
def update_gallery(cls, id, name):
        '''
        Method to update the gallery in the database.
        '''
        return cls.objects.filter(id=id).update(name=name)
 
def __str__ (self):
      return self.name
 
class Photo (models.Model):
     category = models.ForeignKey(Category,on_delete=models.SET_NULL,null=True,blank=True)
     image = CloudinaryField('image')
     description = models.TextField()
     
def save_photo(self):
        '''
        Method to save the image to the database.
        '''
        self.save()

def delete_photo(self):
        '''
        Method to delete the photo from the database.
        '''
        self.delete()
@classmethod
def update_photo(cls, id, image):
        '''
        Method to update the photo in the database.
        '''
        return cls.objects.filter(id=id).update(image=image)
     
def __str__ (self):
      return self.description 

 