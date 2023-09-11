from django.http import JsonResponse
from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import PostSerializer
from .models import Post
# Create your views here.

class TestView(APIView):
    def get(self, request, *args, **kwargs):
        query_set = Post.objects.all()
        result = PostSerializer(instance=query_set,many=True).data
        data = {
        
            'name' : 'Mim Jannat',
            'age' : 25
        }
        return Response(data=result,status=200)
    
    def post(self, request, *args, **kwargs):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.is_valid()
            serializer.save()
            return Response(serializer.data)
        return(serializer.errors)

# def test_view(request):
#     data = {
#         'name': 'Mim Jannat',
#         'age' : 20
#     }
#     return JsonResponse(data)