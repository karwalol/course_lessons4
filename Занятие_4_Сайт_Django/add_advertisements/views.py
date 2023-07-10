from django.shortcuts import render
from django.http import HttpResponse
# место для обработчиков(они получают запрос и формируют ответ)



def index(request):
    return HttpResponse("Привет")