from django import template

register=template.Library()

@register.filter(name='is_in_cart')
def is_in_cart(product,cart):
    key = cart.keys()
    print(key)
    #print(product, cart)
    for i in key:
        if i == 'null':
           print(i)
           i='1'
        else:
           print(i)
           if  int(i) == product.id:
            print(product, cart)
            return True
    return False

@register.filter(name='cart_quantity')
def cart_quantity(product,cart):
    key=cart.keys()
    print(product, cart)
    for i in key:
        if int(i) ==product.id:
            return cart.get(i)
    return 0

@register.filter(name='price_total')
def price_total(product,cart):
    return product.price * cart_quantity(product,cart)

@register.filter(name='total_bill')
def total_bill(product,cart):
    sum=0
    for i in product:
        sum += price_total(i,cart)
    return sum

@register.filter(name='currency')
def currency(number):
    return'₹'+str(number)


@register.filter(name='multiply')
def multiply(n1,n2):
    return n1*n2