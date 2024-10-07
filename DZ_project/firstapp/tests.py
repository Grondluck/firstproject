from django.test import TestCase
from firstapp.models import products
# Create your tests here.

class DiscountTest(TestCase):
  def setUp(self):
    products.objects.create(name="test", count="17",count_left="4",price_selling="200",price_purchase="100",discount2="25")
  def test_discount(self):
    test1 = products.objects.get(name="test")
    self.assertEqual(test1.discount(), 140)
    
интересно, но нифига не понятно)
