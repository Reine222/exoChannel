from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from . import models
import json
from django.http import JsonResponse


# Create your views here.
@login_required
def home(request):
    salon = models.Salon.objects.all()
    salonOne = models.Salon.objects.get(pk=1)

    data={
        'salon': salon,
        'salonOne': salonOne,
    }
    return render(request, "pages/index.html", data)

def salon(request):
    salon = models.Salon.objects.all()
    salonOne = models.Salon.objects.get(pk=1)

    data={
        'salon': salon,
        'salonOne': salonOne,
    }
    return render(request, "pages/salon.html", data)



def loginUser(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        print('******************************************************', username, password )
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('salon')
        else:
            return redirect('login')
    return render(request, "pages/login.html")



def register(request):
    if request.method == "POST" :
        success = False
        username = request.POST.get('username')
        image = request.FILES.get('image')
        password = request.POST.get('password')
        print(username, image)

        if username is not None : 
            user = User(
                username=username,
            )
            try :
                user.save()
                print(user, "**********************************************************************")
                user.profileUser.image=image
                user.profileUser.save()
                user.password=password
                user.set_password(user.password)
                user.save()
                print("*******************************$$$$$$$$$$$$$$$$$$$$$$$$$$$$***************************************")
                prof = models.Profile(image=image)
                print("*******************************$$$$$$$$$$$$$$$$$$$$$$$$$$$$***************************************")
                prof.save()
                print('************************* succes ***********************************')
                success = True
                response = "votre inscription a ete effectuée avec succes"
                return redirect('login')
            except:
                success = False
                response = " error, veillez verifier votre connexion "
    return render(request, "pages/register.html")



def connect(request):
    succes = False
    print('////////////////////////////////////////// REINE //////////////////////////////////////////')
    try:
        print('////////////////////////////////////////// RRRRR //////////////////////////////////////////')
        postdata = json.loads(request.body.decode('utf-8'))
        print('///////////////////////////////////////////////     ZZZZZ     /////////////////////////////////////')
        message = postdata['message']
        print(message,'///////////////////////////////////////////////     ZZZZZ     /////////////////////////////////////')
        username = postdata['username']
        print(username, '////////////////////////////////////////////       $$$$ OK $$$$       ////////////////////////////////////////')
        succes = True
    except Exception as e:
        succes = False
        reponse = "Un probleme survennu lors de l'enregistrement"

    datas = {
        'succes':succes,
    }
    return JsonResponse(datas, safe=False)




def sendsalon(request):
    succes = False
    print('////////////////////////////////////////////////////////////////////////////////////')
    try:
        print('////////////////////////////////////////////////////////////////////////////////////')
        postdata = json.loads(request.body.decode('utf-8'))
        print('////////////////////////////////////////////////////////////////////////////////////')
        nomSal = postdata['nomSal']
        print(nomSal, '////////////////////////////////////////////$$$$ OK $$$$////////////////////////////////////////')
        succes = True
    except Exception as e:
        succes = False
        reponse = "Un probleme survennu lors de l'enregistrement"

    datas = {
        'succes':succes,
    }
    return JsonResponse(datas, safe=False)