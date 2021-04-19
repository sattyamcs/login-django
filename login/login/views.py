from django.shortcuts import render
from login.models import Newuser
from django.contrib import messages


def indexpage(request):
    return render(request, 'index.html')


def registration(request):
    if request.method == "POST":
        Email = request.POST['Email']
        Pwd = request.POST['Pwd']
        Firstname = request.POST['Firstname']
        Lastname = request.POST['Lastname']
        Phone = request.POST['Phone']
        Address = request.POST['Address']
        Gender = request.POST['Gender']

        Newuser(Email=Email, Pwd=Pwd, Firstname=Firstname, Lastname=Lastname,
                Phone=Phone, Address=Address, Gender=Gender).save()
        messages.success(request, 'The new user ' +
                         request.POST['Firstname']+"is saved successfully..!")
        return render(request, 'registration.html')

    else:
        return render(request, 'registration.html')


def loginpage(request):
    if request.method == "POST":
        try:
            UserDetails = Newuser.objects.get(Email=request.POST['Email'],Pwd=request.POST['Pwd'])
            print("Username=", UserDetails)
            request.session['Email'] = UserDetails.Email
            return render(request,'index.html')
        except Newuser.DoesNotExist as e:
            messages.success(request, "Username/Password inavalid..!")
    return render(request,'login.html')


def logout(request):
    try:
        del request.session['Email']
    except:
        return render(request, 'index.html')
    return render(request, 'index.html')
