from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^adminsite/reserveForm/changeForm/(?P<id>[0-9]+)', view=views.reserveForm_change_form, name='ReserveFormChangeForm'),

]