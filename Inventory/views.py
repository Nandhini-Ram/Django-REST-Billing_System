from rest_framework.views import APIView           #for creating API , as Class Based Views
from rest_framework.response import Response       #for Response
from .models import *

# Create your views here.
class ProductView(APIView):

    def get(self, request):
        all_products= Product.objects.all()
        product_data = []

        for product in all_products:
            single_product={
                'id': product.id,
                'product_name': product.product_name,
                'code': product.code,
                'price': product.price
            }
            product_data.append(single_product)
            print(single_product)

        return Response(product_data)

    def post(self, request):

        new_product= Product(product_name=request.data['product_name'], code=request.data['code'],
                            price=request.data['price'])

        new_product.save()   
        return Response("Data saved ")

class ProductViewById(APIView):
    def get(self, request, id):
        product= Product.objects.get(id= id)

        single_product={
                'id': product.id,
                'product_name': product.product_name,
                'code': product.code,
                'price': product.price
            }
        print(single_product)

        return Response(single_product)

    def patch(self, request, id):
        product= Product.objects.filter(id = id) 

        product.update(product_name=request.data['product_name'], code=request.data['code'],
                            price=request.data['price'])

        return Response("Updated")

    def delete(self, request, id):
        product= Product.objects.get(id = id)
        product.delete()

        return Response("Deleted")