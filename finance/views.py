
from django.shortcuts import redirect, render
from finance.models import *

def pay(request):
    ctx = {}
    if request.method == "POST":
        sender = request.POST.get('sender')
        receiver = request.POST.get('receiver')
        amount = request.POST.get('amount')

        amount = float(amount)

        sender_account = Account.objects.get(id=sender)
        receiver_account = Account.objects.get(id=receiver)

        ctx = {"message": "You do not have enough balance to do this transaction", "balance": sender_account.balance}

        if amount <= sender_account.balance:
            sender_transaction = Transaction(account=sender_account, amount= -1 * amount)
            sender_transaction.save()
            sender_account.balance = sender_account.balance - amount
            sender_account.save()

            receiver_transaction = Transaction(account=receiver_account, amount = amount)
            receiver_transaction.save()
            receiver_account.balance = receiver_account.balance +  amount
            receiver_account.save()
            ctx["message"] = "Transaction Successful"
            ctx["balance"] = sender_account.balance

    return render(request, 'payment.html', context=ctx)