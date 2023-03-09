
from django.shortcuts import redirect, render,HttpResponseRedirect
from django.views import View

from .forms import user_model,UserRegisterForm
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    return render(request,'base1.html')

class UserRegister(CreateView):
  template_name = 'register.html'
  success_url = reverse_lazy('login')
  form_class = UserRegisterForm
  success_message = "Your profile was created successfully"


class UserLogin(View):
   
    def get(self,request):
        return render(request,'login.html')

    def post(self,request):
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return render(request,'userhome.html')
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