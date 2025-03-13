from django.test import TestCase
from .models import Deals, Products, News

class DealsTestCase(TestCase):
    def test_create_and_read_deals(self):

        deal_item = Deals.objects.create(
            deal_product_name='Amazing Discount',
            deal_original_price=100,
            deal_new_price=50)

        retrieved_deal = Deals.objects.get(deal_product_name='Amazing Discount')

        self.assertEqual(retrieved_deal.deal_product_name, 'Amazing Discount')
        self.assertEqual(retrieved_deal.deal_original_price, 100)
        self.assertEqual(retrieved_deal.deal_new_price, 50)

        deal_count = Deals.objects.count()
        self.assertEqual(deal_count, 1)

class NewsTestCase(TestCase):
     def test_create_and_read_news(self):
         news_item = News.objects.create(news_title='Breaking News', news_body='News Story')

         retrieved_news = News.objects.get(news_title='Breaking News')

         self.assertEqual(retrieved_news.news_title, 'Breaking News')
         self.assertEqual(retrieved_news.news_body, 'News story.')

class ProductTestCase(TestCase):
    def test_create_product(self):

        product = Products.objects.create(product_name="Test Product", product_price=10.00)

        self.assertEqual(product.product_name, "Test Product")
        self.assertEqual(product.product_price, 10.00)