from .models import ReserveForm, Dookht, Parche, Process, ProcessFormKargar, ServiceTarh, Chap
from UserManager.models import Customer, Kargar
from . import forms

from django.shortcuts import render, redirect, reverse
from django.core.urlresolvers import get_resolver
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login


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
    if request.method == 'POST':
        forms.save_processFormKargar(form, request.POST)
        return redirect(reverse('ReserveFormListAdmin'))
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


def reserveForm_add_form(request):
    if request.method == 'POST':
        form = ReserveForm.objects.create()
        forms.save_reserveForm(form, request.POST)
        return redirect(reverse('ReserveFormListAdmin'))
    customers = Customer.objects.all()
    services = ServiceTarh.objects.all()
    parches = Parche.objects.all()
    dookhts = Dookht.objects.all()
    chaps = Chap.objects.all()
    processes = Process.objects.all()
    context = {'customers':customers, 'parches':parches, 'services':services, 'dookhts':dookhts, 'chaps':chaps,
               'processes':processes, 'daysChoice':dayChoice, 'monthChoice':monthChoice, 'yearChoice':yearChoice}
    return render(request, 'addFormAdminReserveForm.html', context)


def reserveForm_delete(request, id_reserveForm):
    form = ReserveForm.objects.get(id=id_reserveForm)
    form.delete()
    return redirect(reverse('ReserveFormListAdmin'))


def processFormKargar_change_form(request, id_processFormKargar):
    processFormKargar = ProcessFormKargar.objects.get(id=id_processFormKargar)
    processes = Process.objects.all()
    kargars = Kargar.objects.all()
    context = {'processFormkargar':processFormKargar, 'processes':processes, 'kargars':kargars}
    return render(request, 'changeFormAdminProcessReserveKargar.html', context=context)


def processFormKargar_add_form(request, id_reserveForm):
    if request.method == 'POST':
        form = ReserveForm.objects.get(id=id_reserveForm)
        process = ProcessFormKargar.objects.create()
        forms.save_processFormKargar(form, process, request.POST)



def processFormKargar_delete(request, id_processFormKargar):
    process = ProcessFormKargar.objects.get(id=id_processFormKargar)
    form = process.form
    process.delete()
    return redirect(reverse('ReserveFormChangeForm', kwargs={'id_reserveForm':form.id}))


def reserveForm_list_admin(request):
    forms = ReserveForm.objects.all()
    context = {'forms':forms}
    return render(request, 'listAdminReserveForm.html', context=context)



def print_reserve(request, id):
    form = ReserveForm.objects.get(id = id)
    context = {'form':form}
    return render(request, 'printReserve.html', context)



def test(request):
    print('in test func')
    keys = get_resolver(None).reverse_dict.keys()
    for key in keys:
        print(str(key))





@login_required()
def siteadmin(request):
    groups = list(request.user.groups.all())
    for group in groups:
        print('group:'+str(group.name))
    group = ''
    if request.user.is_superuser:
        group = 'superuser'
        print('if1')
    elif groups[0].name == 'admin':
        group = 'admin'
        print('if2')
    elif groups[0].name == 'karbarTehran':
        group = 'karbarTehran'
        print('if3')
    elif groups[0].name == 'karbarKarkhane':
        group = 'karbarKarkhane'
    context = {'group':group}
    return render(request, 'admin/index.html', context)




def loginFunc(request):
    error = ''
    if request.method == 'POST':
        try:
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect(reverse('SiteAdminIndex'))
            else:
                error = 'نام کاربری یا رمز اشتباه است'
        except User.DoesNotExist:
            error = 'نام کاربری یا رمز اشتباه است'
    context = {'error': error}
    return render(request, 'login.html', context)







