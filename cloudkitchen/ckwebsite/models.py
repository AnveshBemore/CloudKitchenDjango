from django.db import models

# Create your models here.
class udetails(models.Model):
    
    uname=models.CharField(max_length=100,default="ck")
    password=models.CharField(max_length=100)
    phnnum=models.IntegerField(null=False,default=0)
    address=models.CharField(max_length=500,null=False,default="")
    def __str__(self):
        return self.uname


class product(models.Model):
    product_id=models.AutoField(primary_key=True)
    product_name=models.CharField(max_length=200,default="",null=False)
    product_price=models.IntegerField(null=False,default=0)
    product_desc=models.CharField(max_length=500,null=True)
    product_img=models.ImageField(upload_to="media")
    product_type=models.CharField(max_length=500,default="",null=False)
    
    def __str__(self):
        return self.product_name
 
class orders(models.Model):
    order_sno=models.AutoField(db_column='order_sno', primary_key=True)
    order_id=models.ForeignKey(product,on_delete=models.CASCADE,null=False,default=0)
    order_name=models.CharField(max_length=200,null=False)
    order_price=models.IntegerField()
    order_img=models.CharField(max_length=200,null=True,default="")
    numofprod=models.IntegerField(null=False,default=1)
    name=models.CharField(max_length=200,null=True,default="")
    def __str__(self):
        return self.order_name

class ordershistory(models.Model):
    order_sno=models.AutoField(db_column='order_sno', primary_key=True)
    order_id=models.ForeignKey(product,on_delete=models.CASCADE,null=False,default=0)
    order_name=models.CharField(max_length=200,null=False)
    order_price=models.IntegerField()
    order_img=models.CharField(max_length=200,null=True,default="")
    numofprod=models.IntegerField(null=False,default=1)
    name=models.CharField(max_length=200,null=True,default="")
    def __str__(self):
        return self.order_name
