from django.shortcuts import render,HttpResponse,redirect
from .models import product,category,customer,orders
from django.contrib.auth.hashers import make_password,check_password
import random
# Create your views here.
def home(req):
    if req.method=="GET":

        cart=req.session.get('cart')
        if not cart:
            req.session['cart']={}
        order = category.getcategory()
        prod=product.getproduct()
        catid=None
        catid=req.GET.get('category')
        print(catid)
        if catid:
            prod=product.getproductbyid(catid)
        else:
            prod=product.getproduct()
        return render(req,'home.html',{'products':prod,'order':order})
    elif req.method=='POST':
        productid=req.POST.get('pid')
        remove=req.POST.get('remove')

        print(productid)

        cart=req.session.get('cart')
        if cart:
            quantity=cart.get(productid)
            if quantity:
                if remove:
                    cart[productid] = quantity - 1
                    if quantity==1:
                        cart.pop(productid)
                else:
                    cart[productid]=quantity+1
            else:
                cart[productid]=1
        else:
            cart={}
            cart[productid] = 1

        req.session['cart']=cart
        print(req.session['cart'])

        return redirect('homepage')


def order(req):
    if req.method=='GET':
        cust=req.session.get('cid')
        print(cust)
        ors=orders.getorder(cust)
        print('aaaa',ors)

        return render(req,'order.html',{'order':ors})
    else:
        pass

def signup(req):
    if req.method=='GET':
        return render(req,'signup.html')
    elif req.method=="POST":
        fname=req.POST.get('firstname')
        lname=req.POST.get('lastname')
        mno=req.POST.get('mobnumber')
        email=req.POST.get('email')
        password=req.POST.get('password')
        c = customer(fname=fname, lname=lname, mobile=mno, email=email, password=password)
        values={'fname':fname,'lname':lname,'mno':mno,'email':email}
        errormsg=None
        exist = c.exist()
        if not fname:
            errormsg="enter first name"
        elif not lname:
            errormsg="enter last name"
        elif not mno:
            errormsg="enter mobile number name"
        elif len(mno)<10 or len(mno)>10:
            errormsg="enter valid number"
        elif not password:
            errormsg="enter password"
        elif len(password)<6:
            errormsg="enter password with atleast 6 chars"
        elif exist==True:
            errormsg="email id exist"

        if errormsg==None:
            c.password=make_password(c.password)
            c.save()
            return redirect('homepage')
        else:
            return render(req,'signup.html',{'error':errormsg,'values':values})

def login(req):
    if req.method=='GET':
        return render(req,'login.html')
    elif req.method=='POST':
        email=req.POST.get('email')
        password=req.POST.get('password')
        c=customer.getcustbyemail(email)
        errormsg = None
        if c:
            ch=check_password(password,c.password)
            if ch:
                req.session['cid']=c.id
                req.session['email'] = c.email

                return redirect('homepage')
            else:
                errormsg = "password is wrong"

        else:
          errormsg="email or password is wrong"

        return render(req,'login.html',{'error':errormsg})
def logout(req):
    req.session.clear()
    return redirect('login')

def cart(req):
    if req.method=="GET":
        id=list(req.session.get('cart').keys())
        ids=[]
        print(id)
        for i in range(len(id)):
            if id[i]=='null':
                break
            else:
                ids.append((id[i]))

        print('asasas',ids)
        pr=product.getproductsforcart(ids)
        print("DDDDD",pr)
    return render(req,'cart.html',{'product':pr})

def checkout(req):
    print(req.method)
    if req.method=='POST':
        print("jhgfdsa")
        address=req.POST.get('address')
        mob=req.POST.get('mob')
        cust=req.session.get('cid')
        prod= product.getproductsforcart( list(req.session.get('cart').keys()))
        print("sdasdasdasdasdasdsdsa",prod)
        cart = req.session.get('cart')
        for i in prod:
            print('iiii',i)
            order=orders(customer=customer(id= cust),price=i.price,mobile=mob,address=address,product=i,quantity=cart.get(str(i.id)))
            order.save()

        req.session['cart']={}

    return render(req,'cart.html')

def profile(req):

    cust = req.session.get('cid')
    print(req.method,cust)
    c=customer.get_cust(cust)
    print(c)
    if req.method=='GET':
        return render(req,'profile.html',{'customer':c})