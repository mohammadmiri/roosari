from . import views

from django.conf.urls import url



urlpatterns = [
    url(r'login/', view=views.loginFunc, name='Login'),
    url(r'reserves/', view=views.show_reserves, name='ShowReserves'),
    url(r'forgetpassword/', view=views.forget_password, name='ForgetPassword'),
    url(r'resetpassword/(?P<id>[0-9]+)/', view=views.reset_password, name='ResetPassword'),
    url(r'test/', view=views.test, name='Test'),
]