from django.shortcuts import render, redirect

def login_page(request):

    if request.method == "POST":

        pin = request.POST.get("pin")

        if pin == "2106":
            return redirect("welcome")

    return render(request, "login.html")


def welcome(request):
    return render(request, "welcome.html")

def memories(request):
    return render(request, 'memories.html')

def celebration(request):
    return render(request, 'celebration.html')

def gallery(request):
    return render(request,'gallery.html')

def final_message(request):
    return render(request, 'final_message.html')

def byee(request):
    return render(request, 'byee.html')