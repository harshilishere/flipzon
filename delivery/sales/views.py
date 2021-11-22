from django.shortcuts import render
from rest_framework import serializers
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.db.models import Q
from django.db.models import F
from .models import newsale,inventory,OrderStatus
from .serializers import NewSaleSerializer, NewInventorySerializer, NewOrderQueueSerializer,NewOrderStatusSerializer

class SaleView(APIView):
    permission_classes = (IsAuthenticated,)
    def get(self,request,*args,**kwargs):
        return Response("Please make a post req with relavant fields")

    def post(self,request,*args,**kwargs):
        serializer = NewSaleSerializer(data=request.data)
        print(request.data["item_model"])
        check = inventory.objects.filter(Q(category=request.data["items_category"]),Q(model_no=request.data["item_model"]),Q(available__gt=0)).exists()
        
        
        if check:
            print(check)
            if serializer.is_valid():
                serializer.save()
                inventory.objects.all().filter(Q(category=request.data["items_category"]),Q(model_no=request.data["item_model"])).update(available=F('available')-request.data["Items_qty"])
                #orderserializer=NewOrderStatusSerializer(data=)
                return Response("Order confirmed")
            return Response (serializer.errors)
        return Response ("Inventory not available")

class InventorySale(APIView):
    permission_classes = (IsAuthenticated,)
    def get(self,request,*args,**kwargs):
        inven = inventory.objects.all()
        serializer=NewInventorySerializer(inven,many=True)
        #return Response("here's all the inventory")
        return Response(serializer.data)

    def post(self,request,*args,**kwargs):
        serializer = NewInventorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response("Inventory updated")
        return Response(serializer.errors)

