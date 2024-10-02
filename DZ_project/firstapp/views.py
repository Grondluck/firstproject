from django.shortcuts import render
from firstapp.models import tags, clients, products
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User



# Create your views here.
def index(request):
    data = tags.objects.all()
    prod = products.objects.all()
    return render(request, "index.html", {"dropdown":data, "product":prod})

def reg(request):
    if request.method == "POST":     
        data = request.POST
        if data["password"] == data ["password_check"]:
            new_user = User.objects.create_user(data["username"], data["email"] , data["password"])
            new_user.save()
            ret = "Вы успешно зарегистрировались!"
            return render(request, "reg.html", {"ret":ret})
        else:
            ret = '<p style="color: red;">Пароли не совпадают</p>'
            return render(request, "reg.html", {"ret":ret})
    else:
        ret = "Регистрация"
        return render(request, "reg.html", {"ret":ret})

def auth(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            username = f"Добро пожаловать, {username}"
            return render(request, "index.html", {"username":username})
        else:
        # Return an 'invalid login' error message.
            error = "Неверно введен логин/пароль"
            return render(request, "auth.html", {"error":error})
    return render(request, "auth.html")