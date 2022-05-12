from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser 
from rest_framework.views import APIView

from gifted.views.services import *

class ChildList(APIView): 
    def get(self, request, format=None):
        data = get_child()
        return Response(data=data)

    def post(self,request,*args,**kwargs):
        data = request.data
        child = post_child(data['name'], data['description'], data['photo'], data['subscription_cost'], data['donee_id'])
        return Response(data=child)

class ChildListInt(APIView):
    def get(self, request, *args, **kwargs):
        child_id = kwargs['child_id']
        data = get_child_int(child_id)
        return Response(data=data)

class ChildListFund(APIView):
    def get(self, request, *args, **kwargs):
        child_id = kwargs['child_id']
        data = get_child_fund(child_id)
        return Response(data=data)