from .models import ReserveForm, Dookht, Parche, Process, ProcessFormKargar, ServiceTarh, Chap
from UserManager.models import Customer, Kargar

from django.shortcuts import render

dayChoice = [
        (1,1),(2,2),(3,3),(4,4),(5,5),(6,6),(7,7),(8,8),(9,9),(10,10),(11,11),(12,12),(13,13),(14,14),(15,15),(16,16),(17,17),(18,18),
        (19, 19), (20, 20), (21, 21), (22, 22), (23, 23), (24, 24), (25, 25), (26, 26), (27, 27), (28, 28), (29, 29), (30, 30), (31, 31),
    ]

monthChoice = [ (1, 'فروردین'), (2, 'اردیبهشت'), (3, 'خرداد'), (4, 'تیر'), (5, 'مرداد'), (6, 'شهریور'), (7, 'مهر'), (8, 'آبان'),
                (9, 'آذر'), (10, 'دی'), (11, 'بهمن'), (12, 'اسفند'),]

yearChoice = [(1395, '۱۳۹۵'), (1396, '۱۳۹۶'), (1397, '۱۹۳۷'), (1398, '۱۳۹۸'), (1399, '۱۳۹۹'), (1400, '۱۴۰۰'), (1401, '۱۴۰۱'),
              (1402, '۱۴۰۲'), (1403, '۱۴۰۳'), (1404, '۱۴۰۴'), (1405, '۱۴۰۵')]

def reserveForm_change_form(request, id):
    form = ReserveForm.objects.get(id=id)
    customers = Customer.objects.all()
    services = ServiceTarh.objects.all()
    formServices = form.serviceTarh.all()
    parches = Parche.objects.all()
    dookhts = Dookht.objects.all()
    chaps = Chap.objects.all()
    processes = Process.objects.all()
    context = {'form':form, 'currentCustomer':form.customer, 'customers':customers, 'services':services, 'formServices':formServices
               , 'parches':parches, 'dookhts':dookhts, 'chaps':chaps, 'daysChoice':dayChoice, 'monthChoice':monthChoice,
               'yearChoice':yearChoice, 'processes':processes}
    return render(request, 'changeFormAdminReserveForm.html', context)



def processFormKargar_change_form(request, id_processFormKargar):
    processFormKargar = ProcessFormKargar.objects.get(id=id_processFormKargar)
    processes = Process.objects.all()
    kargars = Kargar.objects.all()
    context = {'processFormkargar':processFormKargar, 'processes':processes, 'kargars':kargars}
    return render(request, 'changeFormAdminProcessReserveKargar.html', context=context)







