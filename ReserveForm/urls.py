from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^adminsite/reserveForm/changeForm/(?P<id>[0-9]+)', view=views.reserveForm_change_form, name='ReserveFormChangeForm'),
    url(r'^adminsite/reserveForm/list/', view=views.reserveForm_list_admin, name='ReserveFormListAdmin'),
    url(r'^adminsite/reserveForm/addForm/', view=views.reserveForm_add_form, name='ReserveFormAddForm'),
    url(r'^adminsite/reserveForm/delete/(?P<id_reserveForm>[0-9]+)', view=views.reserveForm_delete, name='ReserveFormDelete'),
    url(r'^adminsite/processFormKargar/changeForm/(?P<id_processFormKargar>[0-9]+)', view=views.processFormKargar_change_form, name='ProcessFormKargarChangeForm'),
    url(r'^adminsite/processFormKargar/addForm/', view=views.processFormKargar_add_form, name='ProcessFormKargarAddForm'),
    url(r'^adminsite/processFormKargar/delete/(?P<id_processFormKargar>[0-9]+)', view=views.processFormKargar_delete, name='ProcessFormKargarDelete'),
]