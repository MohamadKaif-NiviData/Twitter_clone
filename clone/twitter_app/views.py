



from django.views import View


from .forms import user_model,UserRegisterForm
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

from django.shortcuts import redirect, render,HttpResponseRedirect

from .forms import user_model
from twitter_app.models import User,Follow

from django.contrib import messages
from django.contrib.auth import authenticate,login,logout

from django.contrib.auth.decorators import login_required

from django.views.generic import TemplateView
from django.contrib.auth import get_user_model
User=get_user_model()
# Create your views here.
class ProfileTemplateView(TemplateView):
    template_name='templates/login.html'
        
def home(request):
    return render(request,'base.html')

class UserRegister(CreateView):
  template_name = 'register.html'
  success_url = reverse_lazy('templates/login/')
  form_class = UserRegisterForm



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


# def userhome(requset):
    # user_info=Tuser.objects.all()
    # form = User.objects.all()
    # f= form.exclude(id=id)
    # cont={'form':f}

# Create your views here.


# def register(request):
#     form=user_model()
#     if request.method == 'POST':
#         username=request.POST.get('username')
#         email=request.POST.get('email')
#         dob=request.POST.get('dob')
#         password=request.POST.get('pass')
        
#         my_user = User.objects.create_user(username,email,password)
#         my_user.save()
#         messages.success(request,'Account is created successfully')

                    
#     cont={'form':form}

#     return render(request,'register.html',cont)

# def Ulogin(request):    
#     if request.method == 'POST':
        
#         username=request.POST.get('username')
#         pass1=request.POST.get('password')
#         user=authenticate(request,username=username,password=pass1)
       
#         if user is not None:
            
#             login(request,user)
#             return redirect('userhome')

    
#     return render (request,'login.html')

def userhome(requset):
  
    return render(requset,'userhome.html')    


# def tweets(request,pk):
#     forms=Tuser_tweets.objects.get(id=pk)
#     form = tweet_modelform(instance=forms)
#     cont={'form':form}
#     return render(request,'tweets.html',cont)     



def userprofile(request,pk):
   
 
    form1= User.objects.get(id=pk)
    is_follow_this_user=False        
    print(form1)
    form= User.objects.exclude(id=pk)
    cont={'form':form,'form1':form1}
    
    
    return render(request,'userprofile.html',cont)




def userhomeside(request):
   
    return render(request,'userhomeside.html')   


def userdyanmicprofile(request,pk):

   
    fr = User.objects.exclude(id=pk)
  
    print(fr)
    cont={'fr':fr}
    return render (request,'userdyanmicprofile.html',cont) 

def followToggle(request,uname):
    pass


class followdoneview(View):
    def post(self,request):
        follower_id= request.POST.get('followed_user_id')
        follower_id_obj = User.objects.get(pk=follower_id)
        try:
            Follow.objects.get(user=request.user,follow=follower_id_obj)
        except Exception as e:
            follow_obj= Follow.objects.create(follow=follower_id_obj) 

        
        return redirect(request.META.get('HTTP_REFERER'))
  

class unfollow_done_view(View):
    def post(self,request):
        unfollower_id= request.POST.get('unfollowed_user_id')
        unfollower_id_obj = User.objects.get(pk=unfollower_id)
        try:
            follo_obj=Follow.objects.get(user=request.user,follow=unfollower_id_obj)
            follo_obj.delete()
        except Exception as e:
            pass

        
        return redirect(request.META.get('HTTP_REFERER'))



   

