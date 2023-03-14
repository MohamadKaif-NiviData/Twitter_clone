
from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import ugettext_lazy
class CustomeManagers(BaseUserManager):
    use_in_migrations = True
    def create_user(self,username,password,**kwars):
        if not username:
            raise ValueError(ugettext_lazy('Enter Valid username'))
        
        user=self.model(username=username,**kwars)
        user.set_password(password)
        user.save(using=self._db)
        return user     
    def create_superuser(self,username,password,**extra_feilds):
        extra_feilds.setdefault('is_active',True)
        extra_feilds.setdefault('is_staff',True)
        extra_feilds.setdefault('is_superuser',True)

        if extra_feilds.get('is_staff') is not True:
            raise ValueError('not valid')
        if extra_feilds.get('is_superuser') is not True:
            raise ValueError('not valid')
        return self.create_user(username,password,**extra_feilds) 