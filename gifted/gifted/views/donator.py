from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser 
from rest_framework.views import APIView

from gifted.views.services import *

class DonatorList(APIView): 
    def get(self, request, format=None):
        data = get_donator()
        return Response(data=data)

    def post(self,request,*args,**kwargs):
        data = request.data
        donator = post_donator(data['name'], data['phone_number'], data['photo'])
        return Response(data=donator)

class DonatorListInt(APIView):
    def get(self, request, *args, **kwargs):
        donator_id = kwargs['donator_id']
        data = get_donator_int(donator_id)
        return Response(data=data)

class DonatorFromName(APIView):
    def get(self, request, *args, **kwargs):
        donator_name = kwargs['donator_name']
        data = get_donator_from_name(donator_name)
        return Response(data=data)