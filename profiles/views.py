from django.shortcuts import render
from profiles.services import create_customer, create_user, username_exists
from finance.services import create_account


def register(request):
    context = {}
    if request.method == "POST":
        name = request.POST.get("name")
        phone = request.POST.get("phone_no")
        address = request.POST.get("address")
        username = request.POST.get("username")
        password = request.POST.get("password")

        if username_exists(username):
            context["message"] = "Username exists. Please choose another username"
        else:
            user = create_user(
                username=username.lower().strip(), password=password.strip()
            )
            customer = create_customer(name, phone, address, user.username)
            create_account(customer_obj=customer)
            context["message"] = f"Your username is {user.username}"
    return render(request, "signup.html", context)
