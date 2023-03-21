




from django.views import View
from django.views.generic.edit import UpdateView

from .forms import UserEditForm,UserRegisterForm
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

from django.shortcuts import redirect, render,HttpResponseRedirect

from .forms import user_model
from twitter_app.models import User,Follow

from django.contrib import messages
from django.contrib.auth import authenticate,login,logout

from django.contrib.auth.decorators import login_required
from django.views import generic
from django.views.generic import TemplateView
from django.contrib.auth import get_user_model
import csv
from django.http import HttpResponse
import io
from django.template.loader import get_template
from xhtml2pdf import pisa
User=get_user_model()
# Create your views here. 


# def user_profile_name(request,username):
#     get_username= User.objects.get(username=username)
    
   
#     cont={'get_username':get_username}
#     return render(request,'user_profile_name.html',cont)

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

def user_home(requset):
  
    return render(requset,'userhome.html')    




def user_profile(request,pk):

    get_user_by_pk= User.objects.get(id=pk)
    is_follow_this_user=False
      
    for Follow_user in request.user.follow_follower.all():
            
            if get_user_by_pk == Follow_user.follow:
                    is_follow_this_user=True   
                    
    
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
   

