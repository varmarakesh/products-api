from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import *
from loader import mongoLoader
import json
import pdb

class DetailView(APIView):

    def get(self, request, id, format = None):
        l = mongoLoader()
        data = l.loadProduct(id)
        l.close()
        if data:
            return Response(data = data, status = HTTP_200_OK)
        else:
            return Response(data = "No product found.", status = HTTP_404_NOT_FOUND)

    def post(self, request, id, format = None):
        return Response(status = HTTP_405_METHOD_NOT_ALLOWED)

    def put(self, request, id, format = None):
        return Response(status = HTTP_405_METHOD_NOT_ALLOWED)

    def delete(self, request, id, format = None):
        return Response(status = HTTP_405_METHOD_NOT_ALLOWED)

class ListView(APIView):

    def get(self, request, format = None):
        l = mongoLoader()
        data = l.loadProducts()
        l.close()
        if data:
            return Response(data = json.loads(data), status = HTTP_200_OK)
        else:
            return Response(data = "No products found", status = HTTP_204_NO_CONTENT)

    def post(self, request, format = None):
        json_data = request.data
        try:
            product_id = json_data['id']
            product_name = json_data['name']
        except KeyError:
            return Response(data = 'Bad Format', status = HTTP_400_BAD_REQUEST)

        l = mongoLoader()
        result = l.saveProduct(id = product_id, name = product_name)
        l.close()

        if result:
            return Response(data = "Product Created", status = HTTP_201_CREATED)
        else:
            return Response("Product with {0} already exists.".format(product_id),status = HTTP_409_CONFLICT)

    def put(self, request,format = None):
        return Response(status = HTTP_405_METHOD_NOT_ALLOWED)

    def delete(self, request, format = None):
        return Response(status = HTTP_405_METHOD_NOT_ALLOWED)