import datetime

from django.db import models

# Create your models here.
odr=0
teamnames=['charlie','alpha']
class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    des = models.TextField()
    date_enrolled = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.name
    
class newsale(models.Model):
    def convertformodel():
        x=datetime.datetime.now()
        x=str(x)
        y=datetime.datetime.strptime(x,"%Y-%m-%d %H:%M:%S.%f")
        global odr
        odr += 1
        order=y.strftime("%d%m%y")+"_"+str(odr)
        print(order)
        return order
        

    order_no = models.CharField(default=convertformodel,null=False,unique=True,max_length=10)
    customer_name = models.CharField(max_length=100)
    customer_add = models.CharField(max_length=500,default=" ")
    dod = models.IntegerField(default=0)
    items_category = models.CharField(max_length=20,default=" ")
    items_qty = models.IntegerField(default=0)
    item_model = models.CharField(max_length=20)
    
    def __str__(self) -> str:
        return self.customer_name

class inventory(models.Model):
    category = models.CharField(max_length=20)
    model_no = models.CharField(max_length=20)
    available = models.IntegerField()
    price = models.IntegerField()

    def __str__(self) -> str:
        return self.category

class OrderQueue(models.Model):        
    order_no = models.IntegerField()
    dod = models.IntegerField()
    team_name = models.CharField(max_length=20)
    ETA = models.DateTimeField()

class OrderStatus(models.Model):
    order_no = models.IntegerField()
    is_assigned = models.BooleanField()
    status = models.TextField()