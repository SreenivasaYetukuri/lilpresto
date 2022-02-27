from statistics import mode
from django.forms import model_to_dict
from django.shortcuts import render
from django.http import JsonResponse, HttpResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response

from products.models import Product
from products.serializers import ProductSerializer

'''
@api_view(["GET"])
def api_home(request, *args, **kwargs):
    """
    DRF API View
    """
    #if request.method != 'POST':
    #    return Response({"detail": "GET Not allowed"}, status=405)
    #model_data= Product.objects.all().order_by("?").first()

    instance  = Product.objects.all().order_by("?").first()
    data = {}
    if instance:
        #data['id'] = model_data.id
        #data["title"] = model_data.title
        #data["content"] = model_data.content
        #data["price"] = model_data.price
        # another method
        #data = model_to_dict(model_data, fields=['id', 'title', 'price', 'sale_price'])
        # in above line, sale_price won't be resulted without serializer since it's property

        data = ProductSerializer(instance).data


    #return JsonResponse(data)
    return Response(data)
'''

@api_view(["POST"])
def api_home(request, *args, **kwargs):
    """
    DRF API View
    """
    # add serilizer
    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        #data = serializer.save()
        #print(data)

        #instance = serializer.save()
        #print(instance)
        print(serializer.data)
        return Response(serializer.data)
    return Response({'invalid': "not a good data"}, status=400)
    