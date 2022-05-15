from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser 
from rest_framework.views import APIView

from gifted.views.services import *

class DoneeList(APIView): 
    def get(self, request, format=None):
        data = get_donee()
        return Response(data=data)

    def post(self,request,*args,**kwargs):
        data = request.data
        donee = post_donee(data['name'], data['phone_number'], data['photo'], data['description'])
        return Response(data=donee)

class DoneeListInt(APIView):
    def get(self, request, *args, **kwargs):
        donee_id = kwargs['donee_id']
        data = get_donee_int(donee_id)
        return Response(data=data)

class DoneeFromName(APIView):
    def get(self, request, *args, **kwargs):
        donee_name = kwargs['donee_name']
        data = get_donee_from_name(donee_name)
        return Response(data=data)

class DoneeListFund(APIView):
    def get(self, request, *args, **kwargs):
        donee_id = kwargs['donee_id']
        data = get_donee_fund(donee_id)
        return Response(data=data)