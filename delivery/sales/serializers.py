from django.db import models
from django.db.models import fields
from rest_framework import serializers
from .models import  newsale, inventory, OrderStatus, OrderQueue


class NewSaleSerializer(serializers.ModelSerializer):
    class Meta:
        model = newsale
        fields=(
            'order_no','customer_name','customer_add','dod','items_category','items_qty','item_model',
        )

class NewInventorySerializer(serializers.ModelSerializer):
    class Meta:
        model = inventory
        fields=(
            'category','model_no','available','price'
        )

class NewOrderStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderStatus
        fields=(
            'order_no','is_assigned','status'
        )

class NewOrderQueueSerializer(serializers.ModelSerializer):
    class Meta:
        models = OrderQueue
        fields=(
            'order_no','dod','team_name','ETA'
        )