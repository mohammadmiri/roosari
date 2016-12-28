from django.conf.urls import url
from django.views.generic.base import RedirectView

from . import views

urlsite = 'http://localhost:8000/'

urlpatterns = [
    url(r'^printForm/(?P<id>[0-9]+)', view=views.print_form, name='PrintReserveForm'),
    url(r'^factorForm/(?P<id>[0-9]+)', view=views.factor_form, name='FactorReserveForm'),
    url(r'^printFormsByOneKargar/(?P<id>[0-9]+)/', view=views.printReserveFormsByOneKargar, name='PrintFormsByOneKargar'),
    url(r'^printFormsInOneProcess/(?P<id>[0-9]+)/', view=views.printReserveFormsInOneProcess, name='PrintFormsInOneProcess'),
    url(r'^printLofOfPForm/(?P<id>[0-9]+)/', view=views.printLogOfProcessOfReserveform, name='PrintLofOfProcessOfRserveForm'),

    # urls of admin of django
    url(r'^redirectToAdminIndex/$', RedirectView.as_view(url=urlsite), name='RedirectToAdminindex'),
    url(r'^siteadmin/$', view=views.siteadmin, name='SiteAdminIndex'),
    url(r'^siteadmin/ReserveForm/ReserveForm/$', RedirectView.as_view(url=urlsite+'admin/ReserveForm/reserveform'), name='changeList_reserveform'),
    url(r'^siteadmin/ReserveForm/ReserveForm/add/$', RedirectView.as_view(url=urlsite+'admin/ReserveForm/reserveform/add/'), name='addform_reserveform'),
    url(r'^siteadmin/ReserveForm/processformkargar/$', RedirectView.as_view(url=urlsite+'admin/ReserveForm/processformkargar'), name='changeList_processformkargar'),
    url(r'^siteadmin/ReserveForm/processformkargar/add/$', RedirectView.as_view(url=urlsite+'admin/ReserveForm/processformkargar/add/'), name='add_processformkargar'),
    url(r'^siteadmin/ReserveForm/dookht/$', RedirectView.as_view(url=urlsite+'admin/ReserveForm/dookht'), name='changeList_dookht'),
    url(r'^siteadmin/ReserveForm/parche/$', RedirectView.as_view(url=urlsite+'admin/ReserveForm/parche'), name='changeList_parche'),
    url(r'^siteadmin/ReserveForm/chap/$', RedirectView.as_view(url=urlsite+'admin/ReserveForm/chap'), name='changeList_chap'),
    url(r'^siteadmin/ReserveForm/process/$', RedirectView.as_view(url=urlsite+'admin/ReserveForm/process'), name='changeList_process'),
    url(r'^siteadmin/ReserveForm/process/reserveProcess/$', RedirectView.as_view(url=urlsite+'admin/ReserveForm/process/2/change/'), name='change_process_reserveProcess'),
    url(r'^siteadmin/ReserveForm/servicetarh/$', RedirectView.as_view(url=urlsite+'admin/ReserveForm/servicetarh'), name='changeList_servicetarh'),
    url(r'^siteadmin/ReserveForm/customer/$', RedirectView.as_view(url=urlsite+'admin/UserManager/customer'), name='changeList_customer'),
    url(r'^siteadmin/ReserveForm/karbarTehran/$', RedirectView.as_view(url=urlsite+'admin/UserManager/karbartehran'), name='changeList_karbarTehran'),
    url(r'^siteadmin/ReserveForm/karbarKarkhane/$', RedirectView.as_view(url=urlsite+'admin/UserManager/karbarkarkhane'), name='changeList_karbarKarkhane'),
    url(r'^siteadmin/ReserveForm/kargar/$', RedirectView.as_view(url=urlsite+'admin/UserManager/kargar'), name='changeList_kargar'),
    url(r'^siteadmin/ReserveForm/otherServices/$', RedirectView.as_view(url=urlsite+'admin/ReserveForm/otherservices'), name='changeList_otherServices'),
    url(r'^siteadmin/logout', RedirectView.as_view(url=urlsite+'admin/logout'), name='adminLogout'),
    url(r'^siteadmin/loginadmin', view=views.loginFunc, name='loginCustomAdmin'),
    url(r'^siteadmin/useradmin', RedirectView.as_view(url=urlsite+'admin/auth/user/'), name='AdminAuthUsers'),
    url(r'^siteadmin/groupadmin', RedirectView.as_view(url=urlsite+'admin/auth/group/'), name='AdminAuthGroups'),
    url(r'^siteadmin/customerMessage/', RedirectView.as_view(url=urlsite+'admin/UserManager/customermessage'), name='changeList_customerMessages')

]