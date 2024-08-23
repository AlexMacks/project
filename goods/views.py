from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def main(request):  
    return HttpResponse("main page")

def info(request):
    return HttpResponse("goods list")

def get_goods_by_id(request, goods_id):
    return HttpResponse(f"Товар: {goods_id}")
