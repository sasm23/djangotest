import json
#from django.http import JsonResponse, HttpResponse
from django.forms.models import model_to_dict
from rest_framework.response import Response
from rest_framework.decorators import api_view

from products.models import Product
from products.serializers import ProductSerializer

@api_view(["GET", "POST"])
def api_home(request, *args, **kwargs):
    #data = request.data
    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        # instance = serializer.save()
        # print(instance)
        print(serializer.data)
        #print(serializer.data)
        #data = serializer.data
        return Response(serializer.data)
    return Response({"invalid": "not good data"}, status=400)

    ''' Below section is for GET request'''
    # instance = Product.objects.all().order_by("?").first()
    # data= {}
    # if instance:
        #data = model_to_dict(instance, fields=['id', 'title', 'price', 'sale_price', 'get_discount'])
        #json_data= json.dumps(data)
        # data["id"]= model_data.id
        # data["title"]= model_data.title
        # data["content"]= model_data.content
        # data["price"]= model_data.price
        # data = ProductSerializer(instance).data
    #return JsonResponse(data)
    # return Response(data)

    # bdy = request.body
    # #print(bdy)
    # data = {}
    # print(request.GET)
    # print(request.POST)
    # try:
    #     data = json.loads(bdy)
    # except:
    #     pass
    # print(data.keys())
    # data['params'] = dict(request.GET)
    # data['headers'] = dict(request.headers)
    # #print(request.headers)
    # data['content-type'] = request.content_type
    # return JsonResponse(data)