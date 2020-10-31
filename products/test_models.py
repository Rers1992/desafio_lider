from django.test import TestCase

# Create your tests here.

from .models import Product

class productsModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        #Set up non-modified objects used by all test methods
        Product.objects.create(brand = 'sfzkvoñ', description = 'descripcion', image = 'url/prueba', price = 1000)

    def test_brand_label(self):
        product = Product.objects.get(id=1)
        field_label = product._meta.get_field('brand').verbose_name
        self.assertEquals(field_label,'brand')

    def test_description_label(self):
        product = Product.objects.get(id = 1)
        field_label = product._meta.get_field('description').verbose_name
        self.assertEquals(field_label,'description')

    def test_image_label(self):
        product = Product.objects.get(id = 1)
        field_label = product._meta.get_field('image').verbose_name
        self.assertEquals(field_label,'image')

    def test_price_label(self):
        product = Product.objects.get(id = 1)
        field_label = product._meta.get_field('price').verbose_name
        self.assertEquals(field_label,'price')

    def test_brand_max_length(self):
        product = Product.objects.get(id = 1)
        max_length = product._meta.get_field('brand').max_length
        self.assertEquals(max_length,50)

    def test_image_max_length(self):
        product = Product.objects.get(id = 1)
        max_length = product._meta.get_field('image').max_length
        self.assertEquals(max_length,255)