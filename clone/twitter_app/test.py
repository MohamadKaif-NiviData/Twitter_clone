
from django.test import SimpleTestCase
from django.test import TestCase,Client
from django.urls import resolve,reverse
from twitter_app.models import User,Follow
from twitter_app.views import user_home,UserTweet,UserEdit,UserRegister




class CheckTestFirstCase(SimpleTestCase):
   



    #url testing 
    def test_check_url(self):
        url = reverse('userhome')
        self.assertEquals(resolve(url).func.view_class,user_home)
    def test_tweet(self):
        url = reverse('usertweet')
        self.assertEquals(resolve(url).func,UserTweet)
    def test_edit(self):
        url = reverse('useredit',args=['pk'])
        self.assertEquals(resolve(url).func.view_class,UserEdit)

class test_views(TestCase):
    def setUp(self):
        self.client = Client()
        self.usertweet = reverse('usertweet')
        self.userretweet= reverse('follow_done_view')
       

    # view test
    def test_view(self):
        

        response = self.client.get(self.usertweet)

        self.assertEquals(response.status_code,200)

        self.assertTemplateUsed(response,'usertweet.html')

   
class test_models(TestCase):   
    # model testing
    def test_user(self):
       user = User.objects.create_user(username='kaif',first_name='kaif92',last_name='asnari',img='def.png',email='kaif23@gmail.com',password='123')
       user1 = User.objects.create_user(username='nividata',first_name='nividata92',last_name='nivi',img='def.png',email='nividata@gmail.com',password='1234')
       user.save()
      
      
       user1.save()
       self.assertEquals(str(user),'kaif')

       follow = Follow(user=user,follow=user1)
       co=User.objects.all()
      
       self.assertEquals(str(follow.user),user.username)
       self.assertEquals(co.count(),2)