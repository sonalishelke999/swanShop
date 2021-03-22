from django.db import models
# Create your models here.
class user(models.Model):
    uid=models.IntegerField()
    ufname=models.CharField(max_length=30)
    ulname=models.CharField(max_length=30)
    uemail=models.EmailField()
    uaddress=models.TextField()
    umobile=models.EmailField()


class category(models.Model):
    name=models.CharField(max_length=30)

    @staticmethod
    def getcategory():
        return category.objects.all()


    def __str__(self):
        return self.name



class product(models.Model):
    pid=models.IntegerField()
    pname=models.CharField(max_length=30)
    category=models.ForeignKey(category,on_delete=models.CASCADE)
    price=models.FloatField()
    description=models.TextField()
    image=models.ImageField(upload_to='static/products',default='null')

    @staticmethod
    def getproduct():
        return product.objects.all()

    @staticmethod
    def getproductbyid(cid):
        if cid:
            return product.objects.filter(category=cid)
        else:
            return product.objects.all()

    @staticmethod
    def getproductsforcart(ids):
        return product.objects.filter(id__in=ids)

class customer(models.Model):
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    email = models.EmailField()
    password = models.CharField(max_length=200)
    mobile = models.CharField(max_length=50)

    def exist(self):
        if customer.objects.filter(email=self.email):
            return True
        else:
            return False
    @staticmethod
    def get_cust(c):
        return customer.objects.get(id=c)

    @staticmethod
    def getcustbyemail(email):
        return customer.objects.get(email=email)

import datetime
class orders(models.Model):
   product= models.ForeignKey(product,on_delete=models.CASCADE)
   customer=models.ForeignKey(customer,on_delete=models.CASCADE)
   quantity=models.IntegerField(default=1)
   price=models.IntegerField()
   date=models.DateField(default=datetime.datetime.today)
   address=models.CharField(max_length=500,default="")
   mobile=models.CharField(max_length=50,default="")
   status=models.BooleanField(default=False)

   @staticmethod
   def getorder(cid):
       print(cid)
       print(cid)
       return orders.objects.filter(customer=cid)
