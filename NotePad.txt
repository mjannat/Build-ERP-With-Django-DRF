from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.

def test_view(request):
    data = {
        'name': 'Mim Jannat',
        'age' : 20
    }
    return JsonResponse(data)