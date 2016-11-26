from django.conf.urls import url
from django.views.generic.base import RedirectView

from . import views

urlsite = 'http://localhost:8000/'

urlpatterns = [
    url(r'^adminsite/reserveForm/changeForm/(?P<id>[0-9]+)', view=views.reserveForm_change_form, name='ReserveFormChangeForm'),
    url(r'^adminsite/reserveForm/list/', view=views.reserveForm_list_admin, name='ReserveFormListAdmin'),
    url(r'^adminsite/reserveForm/addForm/', view=views.reserveForm_add_form, name='ReserveFormAddForm'),
    url(r'^adminsite/reserveForm/delete/(?P<id_reserveForm>[0-9]+)', view=views.reserveForm_delete, name='ReserveFormDelete'),
    url(r'^adminsite/processFormKargar/changeForm/(?P<id_processFormKargar>[0-9]+)', view=views.processFormKargar_change_form, name='ProcessFormKargarChangeForm'),
    url(r'^adminsite/processFormKargar/addForm/', view=views.processFormKargar_add_form, name='ProcessFormKargarAddForm'),
    url(r'^adminsite/processFormKargar/delete/(?P<id_processFormKargar>[0-9]+)', view=views.processFormKargar_delete, name='ProcessFormKargarDelete'),
    url(r'^printForm/(?P<id>[0-9]+)', view=views.print_reserve, name='PrintReserveForm'),
    url(r'test/', view=views.test, name='Test'),

    # urls of admin of django
    url(r'siteadmin/$', view=views.siteadmin, name='SiteAdminIndex'),
    url(r'^siteadmin/ReserveForm/reserveform/$', RedirectView.as_view(url=urlsite+'admin/ReserveForm/reserveform'), name='changeList_reserveform'),
    url(r'^siteadmin/ReserveForm/reserveform/add/$', RedirectView.as_view(url=urlsite+'admin/ReserveForm/reserveform/add/'), name='addform_reserveform'),
    url(r'^siteadmin/ReserveForm/processformkargar/$', RedirectView.as_view(url=urlsite+'admin/ReserveForm/processformkargar'), name='changeList_processformkargar'),
    url(r'^siteadmin/ReserveForm/dookht/$', RedirectView.as_view(url=urlsite+'admin/ReserveForm/dookht'), name='changeList_dookht'),
    url(r'^siteadmin/ReserveForm/parche/$', RedirectView.as_view(url=urlsite+'admin/ReserveForm/parche'), name='changeList_parche'),
    url(r'^siteadmin/ReserveForm/chap/$', RedirectView.as_view(url=urlsite+'admin/ReserveForm/chap'), name='changeList_chap'),
    url(r'^siteadmin/ReserveForm/process/$', RedirectView.as_view(url=urlsite+'admin/ReserveForm/process'), name='changeList_process'),
    url(r'^siteadmin/ReserveForm/servicetarh/$', RedirectView.as_view(url=urlsite+'admin/ReserveForm/servicetarh'), name='changeList_servicetarh'),
    url(r'^siteadmin/ReserveForm/customer/$', RedirectView.as_view(url=urlsite+'admin/UserManager/customer'), name='changeList_customer'),
    url(r'^siteadmin/ReserveForm/karbarTehran/$', RedirectView.as_view(url=urlsite+'admin/UserManager/karbartehran'), name='changeList_karbarTehran'),
    url(r'^siteadmin/ReserveForm/karbarKarkhane/$', RedirectView.as_view(url=urlsite+'admin/UserManager/karbarkarkhane'), name='changeList_karbarKarkhane'),
    url(r'^siteadmin/ReserveForm/kargar/$', RedirectView.as_view(url=urlsite+'admin/UserManager/kargar'), name='changeList_kargar'),
    url(r'^siteadmin/logout', RedirectView.as_view(url=urlsite+'admin/logout'), name='adminLogout'),
    url(r'^siteadmin/loginadmin', view=views.loginFunc, name='loginCustomAdmin'),
    url(r'^siteadmin/useradmin', RedirectView.as_view(url=urlsite+'admin/auth/user/'), name='AdminAuthUsers'),
    url(r'^siteadmin/groupadmin', RedirectView.as_view(url=urlsite+'admin/auth/group/'), name='AdminAuthGroups'),
]