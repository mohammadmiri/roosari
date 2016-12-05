from . import views

from django.conf.urls import url



urlpatterns = [
    url(r'homepage/', view=views.homepage, name='HomepageCustomer'),
    url(r'show_events/', view=views.show_event, name='ShowEvents'),
    url(r'show_reserves/', view=views.show_reserves, name='ShowReserves'),
    url(r'show_profile/', view=views.show_profile, name='ShowProfile'),
    url(r'show_message/(?P<message>.+)/', view=views.show_message, name='ShowMessage'),
    url(r'login/', view=views.loginFunc, name='Login'),
    url(r'reserves/', view=views.show_reserves, name='ShowReserves'),
    url(r'forgetpassword/', view=views.forget_password, name='ForgetPassword'),
    url(r'resetpassword/(?P<id>[0-9]+)/', view=views.reset_password, name='ResetPassword'),
]