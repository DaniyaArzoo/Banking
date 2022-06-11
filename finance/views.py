from django.shortcuts import render
from finance.services import get_account_for_customer, transfer, get_transactions
from django.contrib.auth.decorators import login_required
from profiles.services import get_customer


@login_required
def transfer_money(request):
    ctx = {}

    if request.method == "POST":
        receiver = request.POST.get("receiver")
        amount = request.POST.get("amount")

        user = request.user
        customer = get_customer(user)
        sender_account = get_account_for_customer(customer)
        success, sender_remaining_balance = transfer(
            sender_id=sender_account.id, receiver_id=receiver, amount=amount
        )
        if success:
            ctx["message"] = "Transaction Successful"
        else:
            ctx["message"] = "Insufficient Balance"
        ctx["balance"] = sender_remaining_balance

    return render(request, "payment.html", context=ctx)


@login_required
def passbook(request):
    # Know the account ID
    user = request.user
    customer = get_customer(user)
    account = get_account_for_customer(customer)
    transactions = get_transactions(account_id=account.id)
    # Show Transactions -> In the HTML
    context = {"transactions": transactions, "account": account}
    return render(request, "passbook.html", context)
