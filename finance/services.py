from finance.models import Account, Transaction


def transfer(sender_id, receiver_id, amount):
    amount = float(amount)
    sender_id = int(sender_id)
    receiver_id = int(receiver_id)

    sender_account = get_account(sender_id)
    receiver_account = get_account(receiver_id)

    if amount > sender_account.balance:
        return False, sender_account.balance

    sender_transaction = Transaction(account=sender_account, amount=-1 * amount)
    sender_transaction.save()
    sender_account.balance = sender_account.balance - amount
    sender_account.save()

    receiver_transaction = Transaction(account=receiver_account, amount=amount)
    receiver_transaction.save()
    receiver_account.balance = receiver_account.balance + amount
    receiver_account.save()
    return True, sender_account.balance


def get_transactions(account_id):
    # Get account for this account Id from Account Table
    account = get_account(account_id)
    # Fetch transactions for the account
    transactions = Transaction.objects.filter(account=account).order_by("timestamp")
    return transactions


def get_account(account_id):
    account = Account.objects.get(id=int(account_id))
    return account


def get_account_for_customer(customer_obj):
    account = Account.objects.get(customer=customer_obj)
    return account


def create_account(customer_obj):
    new_account = Account(customer=customer_obj)
    new_account.save()
    return new_account
