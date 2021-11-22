from django.shortcuts import render
from rest_framework import serializers
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated


from sales.serializers import NewOrderStatusSerializer
from sales.models import OrderQueue, newsale, OrderStatus


class Assign(APIView):
    def get(self,request,*args,**kwargs):
        #all_orders = newsale.objects.all()
        #orderserializer=NewOrderStatusSerializer(data=)
        return Response("this is assign api")