from email.mime import image
from unicodedata import category
from django.test import TestCase
from .models import Category,Photo

# Create your tests here.
class CategoryTestClass(TestCase):

    # Set up method
    def setUp(self):
        self.Travel= Category(name = 'Travel')
   # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.Travel,Category))
 
   # Testing Save Method
    def test_save_method(self):
        self.Travel.save_gallery()
        category = Category.objects.all()
        self.assertTrue(len(category) > 0)
    
  # Testing Delete Method
    def test_delete_method(self):
        self.Travel.delete_gallery()
        category = Category.objects.all()
        self.assertTrue(len(category) > 0)
    
    # Testing Update Method
    def test_update_method(self):
        self.Travel.update_gallery()
        category = Category.objects.all()
        self.assertTrue(len(category) > 0)
        
    def save_gallery(self):
        self.save()
        
    def delete_gallery(self):
        self.delete()
        
    def update_gallery(self):
        self.update()
  
class PhotoTestClass(TestCase):

    # Set up method
    def setUp(self):
        self.Travel= Category(category = 'Travel',image="travel.jpg",description="The most beautiful thing in the world is, of course, the world itself – Wallace Stevens")
        
   # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.Travel,Photo))
        
 # Testing Delete Method
    def test_delete_method(self):
        self.Travel.delete_photo()
        category = Category.objects.all()
        self.assertTrue(len(category) > 0)
    
    # Testing Update Method
    def test_update_method(self):
        self.Travel.update_photo()
        category = Category.objects.all()
        self.assertTrue(len(category) > 0)
        
    