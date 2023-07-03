
from audioop import reverse

from django.utils import translation
from typing_extensions import Self
from django import template
from django import views
from django.template import loader
from django.views import View
from django.views.generic.edit import UpdateView
from django.urls import reverse
from django.utils.translation import activate
from .forms import UserEditForm,UserRegisterForm,UserTweetForm
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .serializer import  LikeSerializer,TweetSerializer,ReTweetSerializer
from django.shortcuts import redirect, render,HttpResponseRedirect
from rest_framework import  viewsets
from .forms import user_model
from rest_framework import generics
from twitter_app.models import ReTweet, User,Follow,Tweet,Like,ReTweet
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

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
from translate import Translator
from django.contrib import  messages
User=get_user_model()

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

    def get(self,request):
       
        user=request.user
        
        # retweet_show = ReTweet.objects.all()
        tweet_show = Tweet.objects.all()
        
        
        current_user = request.user
        current_user_remove = User.objects.exclude(id=current_user.id)
       
        
        cont={'tweet_show':tweet_show,'current_user_remove':current_user_remove,'user':user}
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
        print(follower_id_obj,'id with info')
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
    if request.method == 'POST':
        tweet_id = request.POST.get('tweet_id')
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

def logout_user(request):

    logout(request)
    return redirect('login')      
        
def set_lenguage(request):
    if request.method == 'POST' :
        language_code = request.POST.get('language')
        print(language_code)
        if language_code == 'en':
            user_language='en'
            translation.activate(user_language)
            return redirect(request.META.get('HTTP_REFERER'))  
        else:
            user_language='hi'
            translation.activate(user_language)
            tweet_show = Tweet.objects.all()
            cont= {'tweet_show':tweet_show}
            return render(request,'translate_hindi.html',cont)
    else:

       
        user_language='en'
        translation.activate(user_language)
        return render(request,'userhome.html')

    
def Delete_post(request):
    post_id = request.POST.get('post_id')
    del_post = Tweet.objects.get(id=post_id)
    del_post.delete()
    return redirect(request.META.get('HTTP_REFERER'))   


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

from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404
from rest_framework.parsers import MultiPartParser,FormParser
@api_view(['POST'])
def Post(request):
    print('1')
    user = request.user
    user_id = request.user.id

    tweet_id = request.data["tweet"]

    print(request.data)
    print(tweet_id,'t_id')
    tweet_obj = Tweet.objects.get(pk=tweet_id)
    print(tweet_obj.liked.all() ,'this is all data')
    if user in tweet_obj.liked.all():
            print('remove call')

            tweet_obj.liked.remove(user)
            print(tweet_obj.liked.all(),'after remove call')
    else:
            print('add call')

            tweet_obj.liked.add(user)
            print(tweet_obj.liked.all(),'after add call')

    like,create = Like.objects.get_or_create(tweet=tweet_obj, user=user)
    print(like,'like')
    print(create,'create')
    if not create:
        if like.value == 'Like':
            like.value = 'Unlike'
            print(like.value,'when not create')
        else:
            like.value = 'Like'
            print(like.value,'when create')
    like.save()

    ser = LikeSerializer(data=request.data)

    if ser.is_valid():


            return Response(ser.data)
    else:
            return HttpResponse('<h1>Not Accepted data Please check again!</h1>')
@api_view(['GET','POST'])
def LikeList(request):

    like_list = Like.objects.all()
    if like_list:
        like_obj = LikeSerializer(like_list,many=True)
        return  Response(like_obj.data)
@api_view(['POST'])
def Retweet_Post(request):
    user = request.user
    user_id = user.id
    tweet_id = request.data["tweet"]
    tweet_obj = Tweet.objects.get(id=tweet_id)
    if user in tweet_obj.retweet.all():
        tweet_obj.retweet.remove(user)
    else:
        tweet_obj.retweet.add(user)
    retweet, create = ReTweet.objects.get_or_create(tweet=tweet_obj, user=user)
    if not create:
        if retweet.value == 'ReTweet':
            retweet.value = 'Remove'
        else:
            retweet.value = 'ReTweet'
    retweet.save()
    ser = ReTweetSerializer(data=request.data)
    if ser.is_valid():

        return Response(ser.data)
    else:
        return HttpResponse('<h1>Not Accepted data Please check again!</h1>')

@api_view(['GET'])
def Retweet_List(request):
    queryset = ReTweet.objects.all()
    seriallizer_class = ReTweetSerializer(queryset,many=True)
    return  Response(seriallizer_class.data)


@api_view(['DELETE'])
def delete_post(request,id):
    Tweet_id = Tweet.objects.get(id=id)
    tweet_obj = Tweet_id.delete()
    return HttpResponse('data Delete')


@api_view(['POST'])
def Tweet_Post(request):
    # parser_classes = (MultiPartParser,FormParser,)
    print("call")
    print(request.data['user'])
    print(request.data)
    ser = TweetSerializer(data=request.data)
    print(ser)
    if ser.is_valid():
            ser.save()
            print('save data')
            return redirect('userhome')
    else:
            return HttpResponse('data not correct')

@api_view(['GET'])
def Tweet_List(request):
    tweet_list = Tweet.objects.all()
    if tweet_list:
        serializer_class = TweetSerializer(tweet_list,many=True)
        return Response(serializer_class.data)