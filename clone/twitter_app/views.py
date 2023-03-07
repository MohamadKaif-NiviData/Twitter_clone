from django.shortcuts import redirect, render,HttpResponseRedirect

from .forms import user_model

from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
# Create your views here.
def home(request):
    return render(request,'base.html')

def register(request):
    form=user_model()
    if request.method == 'POST':
        username=request.POST.get('username')
        email=request.POST.get('email')
        dob=request.POST.get('dob')
        password=request.POST.get('pass')
        
        my_user = User.objects.create_user(username,email,password)
        my_user.save()
        messages.success(request,'Account is created successfully')

                    
    cont={'form':form}

    return render(request,'register.html',cont)

def Ulogin(request):    
    
  
    if request.method == 'POST':
        
        username=request.POST.get('username')
        pass1=request.POST.get('password')
        user=authenticate(request,username=username,password=pass1)
       
        if user is not None:
            
            login(request,user)
            return redirect('userhome')

    
    return render (request,'login.html')
@login_required(login_url='Ulogin')
def userhome(requset):
    # user_info=Tuser.objects.all()
    
    # cont={'user_info':user_info}
    return render(requset,'userhome.html')    


# def tweets(request,pk):
#     forms=Tuser_tweets.objects.get(id=pk)
#     form = tweet_modelform(instance=forms)
#     cont={'form':form}
#     return render(request,'tweets.html',cont)     


def userprofile(request):
    return render(request,'userprofile.html')


def userhomeside(request):
    return render(request,'userhomeside.html')    