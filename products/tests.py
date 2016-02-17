import unittest
import requests
from sqlalchemy import *
from sqlalchemy.orm import sessionmaker
from loader import mongoLoader

class test(unittest.TestCase):
    def test_get(self):
        url = 'http://127.0.0.1:8000/test/1'
        r = requests.get(url = url)
        self.assertTrue('loaf of bread' in r.content)
        self.assertEqual(r.status_code, 200)

    def test_product_load(self):
        l = mongoLoader()
        products = l.loadProducts()
        self.assertEqual(products[0]['name'], 'loaf of bread')

    def test_single_product_load(self):
        l = mongoLoader()
        product = l.loadProduct(id = 1)
        self.assertEqual(product['name'], 'loaf of bread')

    def test_save_product(self):
        l = mongoLoader()
        self.assertTrue(l.saveProduct(id = 2, name = 'bananas'))
