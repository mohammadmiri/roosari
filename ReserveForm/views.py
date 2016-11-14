from .models import ReserveForm, Dookht, Parche, Process, ProcessFormKargar, ServiceTarh
from UserManager.models import Customer

from django.shortcuts import render



def reserveForm_change_form(request, id):
    form = ReserveForm.objects.get(id=id)
    customers = Customer.objects.all()
    services = ServiceTarh.objects.all()
    formServices = form.serviceTarh.all()
    context = {'currentCustomer':form.customer, 'customers':customers, 'services':services, 'formServices':formServices}
    return render(request, 'siteAdmin/ReserveForm/change_form.html', context)











