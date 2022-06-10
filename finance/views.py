
from django.shortcuts import redirect,render
from django.contrib import messages
from .models import *
from django.db import transaction

def pay(request):
    if request.method=="POST":
        try:
            Sender=request.POST.get('Sender')
            Receiver=request.POST.get('Receiver')
            amt=request.POST.get('Amount')
            with transaction.atomic():
                Sender.obj=transaction.objects.get(user=Sender)
                Sender.obj.amt-=int(amt)
                Sender.obj.save()

                Receiver.obj=transaction.objects.get(user=Receiver)
                Receiver.obj.amt+=int(amt)
                Receiver.obj.save()
                messages.success(request,"Your Amount Transferred Successfully!")

        except Exception as e:
            print(e)
            messages.success(request,"OOPS! Something went wrong.")
        return redirect('/')
    
    return render(request,'payment.html')