import unittest

class tests(unittest.TestCase):

    def test_mongo_connection(self):
        from pymongo import MongoClient
        from pymongo.errors import ConnectionFailure
        try:
            mongoDB = MongoClient(['52.24.167.192:27017'])['productDB']
            if mongoDB:
                self.assertTrue(True)
        except ConnectionFailure:
            self.assertTrue(False)

    def test_product_creation(self):
        from products.loader import mongoLoader
        import requests
        l = mongoLoader()
        id = l.generateId()
        post_url = "http://127.0.0.1:8000/products/"
        payload = {
            "id":id,
            "name":'apricots'
        }
        r = requests.post(url = post_url, data = payload)
        self.assertEqual(r.status_code, 201)
        print 'Product with Id {0} successfully created (http post).'.format(id)

        get_url = "http://127.0.0.1:8000/products/{0}".format(id)
        r = requests.get(url = get_url)
        self.assertEqual(r.status_code, 200)
        print 'Product with Id {0} successfully retrieved (http get).'.format(id)


