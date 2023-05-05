from django.test import TestCase

from desi_mart.models import Category, Product


class TestCategoriesModel(TestCase):

    def setUp(self):
        self.data1 = Category.objects.create(name='Spices')

    def test_category_model_entry(self):
        """
        Test Category model data insertion/types/field attributes
        """
        data = self.data1
        self.assertTrue(isinstance(data, Category))
        self.assertEqual(str(data), 'Spices')


class TestProductsModel(TestCase):
    def setUp(self):
        Category.objects.create(name='Spices')
        self.data1 = Product.objects.create(category_id=1, title='cinnamon',
                                            price='20.00', discount_price='10.00', imageLink='django.com')

    def test_products_model_entry(self):
        """
        Test product model data insertion/types/field attributes
        """
        data = self.data1
        self.assertTrue(isinstance(data, Product))
        self.assertEqual(str(data), 'cinnamon')