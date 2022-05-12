from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser 
from rest_framework.views import APIView

from gifted.views.services import *

class SubscriptionList(APIView): 
    def get(self, request, format=None):
        child_id = request.GET['child_id']
        donator_id = request.GET['donator_id']
        data = get_subscription(child_id, donator_id)
        return Response(data=data)

    def post(self,request,*args,**kwargs):
        data = request.data
        subscription = post_subscription(data['child_id'], data['donator_id'])
        return Response(data=subscription)

class SubscriptionListDonator(APIView):
    def get(self, request, *args, **kwargs):
        donator_id = kwargs['donator_id']
        data = get_subscription_donator(donator_id)
        return Response(data=data)

class SubscriptionListChild(APIView):
    def get(self, request, *args, **kwargs):
        child_id = kwargs['child_id']
        data = get_subscription_child(child_id)
        return Response(data=data)

class SubscriptionListDonee(APIView):
    def get(self, request, *args, **kwargs):
        donee_id = kwargs['donee_id']
        data = get_subscription_donee(donee_id)
        return Response(data=data)