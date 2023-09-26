from django.shortcuts import render,redirect
import razorpay
from ecommerce.settings import RAZORPAY_API_KEY,RAZORPAY_API_SECRET_KEY

# Create your views here.
def payout(request):
    
    client = razorpay.Client(auth=(RAZORPAY_API_KEY, RAZORPAY_API_SECRET_KEY))
    DATA = {
            "amount": 3000,
            "currency": "INR",
            "receipt": "receipt#1",
            "notes": {
                "key1": "value3",
                "key2": "value2"
            }
        }
    order=client.order.create(data=DATA)
    order_id=order['id']
    print('********************')
    print(f'orderID: {order_id}')
    print(f'orderID: {order_id}')
    print('********************')
    print('********************')
    
    context={
        'amount':500,'api_key':RAZORPAY_API_KEY,'order_id':order_id,'name':'Roshith'
    }
    return render(request,'payout.html',context)




def index(request):
    return render(request,'index.html')

    





