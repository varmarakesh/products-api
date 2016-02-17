from pymongo import MongoClient
from bson.json_util import dumps

class mongoLoader:

    def __init__(self):
        self.client = MongoClient(['52.24.167.192:27017'])
        self.db = self.client['productDB']
        self.products = self.db['products']

    def loadProducts(self):
        entity = self.products.find({}, {'_id': False})
        self.client.close()
        return dumps(entity)

    def loadProduct(self, id):
        entity = self.products.find_one({'id':int(id)}, {'_id': False})
        self.client.close()
        return entity

    def saveProduct(self, id, name):
        id_list = map(lambda p:int(p['id']), self.products.find())
        if id in id_list:
            return False
        else:
            self.products.insert({'id':int(id), 'name':name})
            return True

    def generateId(self):
        """ Generates the Id based on the highest id saved in the mongo product collection.
        """
        id = max(map(lambda p:int(p['id']), self.products.find()))+1
        self.close()
        return id

    def close(self):
        self.client.close()

