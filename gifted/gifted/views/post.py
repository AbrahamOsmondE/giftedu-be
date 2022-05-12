from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser 
from rest_framework.views import APIView

from gifted.views.services import *

class PostList(APIView): 
    def get(self, request, format=None):
        data = get_post()
        return Response(data=data)

    def post(self,request,*args,**kwargs):
        data = request.data
        post = post_post(data['title'], data['text'], data['child_id'])
        return Response(data=post)

class PostListInt(APIView):
    def get(self, request, *args, **kwargs):
        post_id = kwargs['post_id']
        data = get_post_int(post_id)
        return Response(data=data)