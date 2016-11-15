from .models import ReserveForm, Dookht, Parche, Process, ProcessFormKargar, ServiceTarh, Chap
from UserManager.models import Customer

from django.shortcuts import render

dayChoice = (
        (1,1),(2,2),(3,3),(4,4),(5,5),(6,6),(7,7),(8,8),(9,9),(10,10),(11,11),(12,12),(13,13),(14,14),(15,15),(16,16),(17,17),(18,18),
        (19, 19), (20, 20), (21, 21), (22, 22), (23, 23), (24, 24), (25, 25), (26, 26), (27, 27), (28, 28), (29, 29), (30, 30), (31, 31),
    )

monthChoice = ( (1, 'فروردین'), (2, 'اردیبهشت'), (3, 'خرداد'), (4, 'تیر'), (5, 'مرداد'), (6, 'شهریور'), (7, 'مهر'), (8, 'آبان'),
                (9, 'آذر'), (10, 'دی'), (11, 'بهمن'), (12, 'اسفند'),
    )

year = ()

def reserveForm_change_form(request, id):
    form = ReserveForm.objects.get(id=id)
    customers = Customer.objects.all()
    services = ServiceTarh.objects.all()
    formServices = form.serviceTarh.all()
    parches = Parche.objects.all()
    dookhts = Dookht.objects.all()
    chaps = Chap.objects.all()
    context = {'form':form, 'currentCustomer':form.customer, 'customers':customers, 'services':services, 'formServices':formServices
               , 'parches':parches, 'dookhts':dookhts, 'chaps':chaps, }
    return render(request, 'siteAdmin/ReserveForm/change_form.html', context)











