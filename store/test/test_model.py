from django.test import TestCase
from store.models import category,Product

class TestCategoriesModel(TestCase):

    def setUp(self):
        self.data1 = category.objects.create(name='django', slug ='django')

    def test_category_model_entry(self):

        data= self.data1
        self.assertTrue(isinstance(data,category))
        
