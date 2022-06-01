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