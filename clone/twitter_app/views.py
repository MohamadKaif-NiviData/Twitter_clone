
from audioop import reverse
from typing_extensions import Self
from django import template
from django import views
from django.template import loader
from django.views import View
from django.views.generic.edit import UpdateView

from .forms import UserEditForm,UserRegisterForm,UserTweetForm
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

from django.shortcuts import redirect, render,HttpResponseRedirect

from .forms import user_model
from twitter_app.models import ReTweet, User,Follow,Tweet,Like,ReTweet

from django.contrib import messages
from django.contrib.auth import authenticate,login,logout

from django.contrib.auth.decorators import login_required
from django.views import generic
from django.views.generic import TemplateView
from django.contrib.auth import get_user_model
import csv
from django.http import HttpResponse, request
import io
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.utils.translation import gettext as _
User=get_user_model()
tweet_id=0
# Create your views here. nivi_CGsR08K.jpeg


def user_profile_name(request,username):
    get_username= User.objects.get(username=username)
   
    cont={'get_username':get_username}
    print(cont)
    return render(request,'user_profile_name.html',cont)

class ProfileTemplateView(TemplateView):
    template_name='templates/login.html'
        
def home(request):
    return render(request,'base.html')

class UserRegister(generic.CreateView):
  form_class = UserRegisterForm
  template_name = 'register.html'
  success_url = reverse_lazy('login')
 
  

def user_converte_pdf(request):
    follow= Follow.objects.all()

    template_path = 'userconvertepdf.html'
    context = {'follow': follow}
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="report.pdf"'
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
       html, dest=response)
    # if error then show some funny view
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response



def user_converte_csv(request,pk):
    response = HttpResponse(content_type='text/csv')
    response['content-disposition']='attachment;filename=followerse.csv'

    writer = csv.writer(response)

    follows= Follow.objects.all()
    writer.writerow(['Followerse','Following'])
    for f in follows:
        writer.writerow([f.user,f.follow])
    return response
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
class user_home(View):
    template_name='userhome.html'
    def get(self,request,*args,**kwargs):
       
        user=request.user
        
        # retweet_show = ReTweet.objects.all()
        tweet_show = Tweet.objects.all()
       
        trans = _('User')
        current_user = request.user
        current_user_remove = User.objects.exclude(id=current_user.id)
       
        
        cont={'tweet_show':tweet_show,'current_user_remove':current_user_remove,'user':user,'trans':trans}
        return render(request,self.template_name,context=cont) 
# def user_home(response):
    
    
    
#     print(response.user,'from home user')
#     # is_like_this_post=False
#     # if tweet_id != 0:
#     #     try:
#     #         Like.objects.get(user=response.user,tweet_id=tweet_id)
#     #         is_like_this_post=True   
#     #     except Exception as e:
#     #         is_like_this_post=False
#     # print(is_like_this_post)        
   
#     return render(response,'userhome.html',cont)    




def user_profile(request,pk):

    get_user_by_pk= User.objects.get(id=pk)
    
      
    try:
        Follow.objects.get(user=request.user,follow=get_user_by_pk)
        is_follow_this_user=True   
    except Exception as e:
       is_follow_this_user=False

    # for Follow_user in request.user.follow_follower.all():
            
    #         if get_user_by_pk == Follow_user.follow:
                    
                    
    
    exclude_user_by_pk= User.objects.exclude(id=pk)
       
    cont={'exclude_user_by_pk':exclude_user_by_pk,'get_user_by_pk':get_user_by_pk,'is_follow_this_user':is_follow_this_user}
    
    
    return render(request,'userprofile.html',cont)




def user_home_side(request):
   
    return render(request,'userhomeside.html')   


class FollowDoneView(View):
    def post(self,request):
        follower_id= request.POST.get('followed_user_id')
        follower_id_obj = User.objects.get(pk=follower_id)
        
        try:
            Follow.objects.get(user=request.user,follow=follower_id_obj)
        except Exception as e:
            follow_obj= Follow.objects.create(follow=follower_id_obj) 

        
        return redirect(request.META.get('HTTP_REFERER'))
  

class UnfollowDoneView(View):
    def post(self,request):
        unfollower_id= request.POST.get('unfollowed_user_id')
        unfollower_id_obj = User.objects.get(pk=unfollower_id)
        try:
            follo_obj=Follow.objects.get(user=request.user,follow=unfollower_id_obj)
            follo_obj.delete()
        except Exception as e:
            pass

        
        return redirect(request.META.get('HTTP_REFERER'))


class UserEdit(UpdateView):
    model=User
    fields=['username','first_name','last_name','img','email']
    
    template_name='useredit.html'
    success_url=reverse_lazy('userhome')

    # def get_obj(self):
    #     return self.request.user
   
def UserTweet(request):
    template = loader.get_template('usertweet.html')
    form_class=UserTweetForm
    cont={'form':form_class}
    return  HttpResponse(template.render(cont,request))

class post_create_view(View):
    form_class=UserTweetForm
    def post(self,request):
        form = self.form_class(request.POST,request.FILES)
        
        if form.is_valid():
            form.save() 
            return redirect('userhome')


def post_like_view(request):
    user = request.user
    print(user)
    if request.method == 'POST':
        
        tweet_id = request.POST.get('tweet_id')
        print(tweet_id)
        tweet_obj = Tweet.objects.get(id=tweet_id)
        if user in tweet_obj.liked.all():
            tweet_obj.liked.remove(user)
        else:
            tweet_obj.liked.add(user)

        like,create = Like.objects.get_or_create(tweet_id=tweet_id,user=user) 

        if not create:
            if like.value == 'Like':
                like.value = 'Unlike'
            else:
                like.value = 'Like'
        like.save()


    return redirect(request.META.get('HTTP_REFERER'))   


def user_retweet(request):
    user = request.user
    if request.method == 'POST':
        tweet_id = request.POST.get('retweet_id')
        print(tweet_id)
        tweet_obj = Tweet.objects.get(id=tweet_id)
        print(tweet_obj)
        if user in tweet_obj.retweet.all():
            tweet_obj.retweet.remove(user)
            print('y')
        else:
            tweet_obj.retweet.add(user)


        retweet,create = ReTweet.objects.get_or_create(tweet_id=tweet_id,user=user)
        if not create:
            if retweet.value == 'ReTweet':
                retweet.value = 'Remove'
            else:
                retweet.value = 'ReTweet'
        retweet.save()
    return redirect(request.META.get('HTTP_REFERER'))  

# class post_like_view(View):
    
#     def post(self,request,*args,**kwargs):
#        

        
        
               




# class post_unlike_view(View):
#   def post(self,request,*args,**kwargs):
#         global tweet_id
#         tweet_id=kwargs.get('id')
#         try:
#             like_obj=Like.objects.get(tweet_id=tweet_id,user_id=request.user)
#             like_obj.delete()
#         except Exception as e:
#            pass
#         return redirect(request.META.get('HTTP_REFERER'))   
