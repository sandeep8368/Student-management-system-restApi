# from django.shortcuts import render
# from django.http import HttpResponse
from rest_framework import viewsets
from app.models import studentModel
from app.serializers import studentSerializers

# Create your views here.
# def display_view(request):
#     return HttpResponse("This is django....")


class studentViewset(viewsets.ModelViewSet):
    queryset = studentModel.objects.all()
    serializer_class = studentSerializers