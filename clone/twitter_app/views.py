

from django.shortcuts import redirect, render,HttpResponseRedirect
from django.views import View


from .forms import user_model,UserRegisterForm
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

from django.shortcuts import redirect, render,HttpResponseRedirect

from .forms import user_model


from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from django.views.generic import TemplateView

# Create your views here.
class ProfileTemplateView(TemplateView):
    template_name='registration/login.html'
        
def home(request):
    return render(request,'base1.html')

class UserRegister(CreateView):
  template_name = 'register.html'
  success_url = reverse_lazy('accounts/login')
  form_class = UserRegisterForm
  success_message = "Your profile was created successfully"


# class UserLogin(View):
   
#     def get(self,request):
#         return render(request,'login.html')

#     def post(self,request):
#         username=request.POST['username']
#         password=request.POST['password']
#         user=authenticate(request,username=username,password=password)
#         if user is not None:
#             login(request,user)
#             return render(request,'userhome.html')
#         return render (request,'login.html')        

@login_required(login_url='Ulogin')
# def userhome(requset):
    # user_info=Tuser.objects.all()
    # form = User.objects.all()
    # f= form.exclude(id=id)
    # cont={'form':f}

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



def userprofile(request,pk):
    
    form = User.objects.all()
    f= form.exclude(id=pk)
    cont={'form':f}
    return render(request,'registration/userprofile.html',cont)


def userhomeside(request):
    return render(request,'userhomeside.html')   


def userdyanmicprofile(request,pk):

   
    fr = User.objects.filter(id=pk)
    f=fr.values_list('username','email','first_name','last_name')
    print(f)
    cont={'f':f}
    return render (request,'userdyanmicprofile.html',cont) 



def followToggle(request,pk):

    pass

    form=User.objects.filter(id=pk)
    # form = f.filter(id=pk)
    cont={'form':form}
    return render (request,'userdyanmicprofile.html',cont)     

    pass

def userprofile(request):
    return render(request,'userprofile.html')


def userhomeside(request):
    return render(request,'userhomeside.html')    

