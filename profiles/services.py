from django.contrib.auth.models import User
from profiles.models import Customer
from django.contrib.auth.hashers import make_password


def create_user(username, password):
    username = username.lower().strip()
    password = password.strip()
    new_user = User(username=username, password=make_password(password))
    new_user.save()
    return new_user


def username_exists(username):
    username = username.lower().strip()
    user_exists = User.objects.filter(username=username).exists()
    return user_exists


def get_user(username):
    user = User.objects.get(username=username)
    return user


def create_customer(name, phone, address, username):
    user = get_user(username)
    new_customer = Customer(
        name=name.strip(), phone_no=phone.strip(), address=address.strip(), user=user
    )
    new_customer.save()
    return new_customer


def get_customer(user_obj):
    customer = Customer.objects.get(user=user_obj)
    return customer
