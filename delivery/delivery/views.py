from django.shortcuts import render
from rest_framework import serializers
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated


from sales.serializers import StudentSerializer,NewOrderStatusSerializer
from sales.models import Student
from sales.models import OrderQueue, newsale, OrderStatus

class TestView(APIView):
    permission_classes = (IsAuthenticated,)
    def get(self,request,*args,**kwargs):
        qs=Student.objects.all()
        student1 = qs.first()
        serializer = StudentSerializer(student1)
        return Response(serializer.data)

    def post(self,request,*args,**kwargs):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response (serializer.errors)

class Assign(APIView):
    def get(self,request,*args,**kwargs):
        #all_orders = newsale.objects.all()
        #orderserializer=NewOrderStatusSerializer(data=)
        return Response("this is assign api")