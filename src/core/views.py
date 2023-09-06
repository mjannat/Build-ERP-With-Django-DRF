from django.http import JsonResponse
from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import PostSerializer
from .models import Post
# Create your views here.

class TestView(APIView):
    def get(self, request, *args, **kwargs):
        data = {
        
            'name' : 'Mim Jannat',
            'age' : 25
        }
        return Response(data)
    
    def post(self, request, *args, **kwargs):
        serializer = PostSerializer(data=request.data)
        serializer.is_valid()
        serializer.save()
        return Response(serializer.data)

# def test_view(request):
#     data = {
#         'name': 'Mim Jannat',
#         'age' : 20
#     }
#     return JsonResponse(data)