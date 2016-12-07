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



@login_required(login_url='/')
def siteadmin(request):
    groups = list(request.user.groups.all())
    group = ''
    if request.user.is_superuser:
        group = 'superuser'
    elif groups[0].name == 'admin':
        group = 'admin'
    elif groups[0].name == 'karbarTehran':
        group = 'karbarTehran'
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
    return render(request, 'admin/login.html', context)



def print_form(request, id):
    pass


def factor_form(request, id):
    form = ReserveForm.objects.get(id=id)
    context = {'form':form}
    return render(request, 'printFactorReserve.html', context=context)



def printReserveFormsByOneKargar(request, id):
    karger = Kargar.objects.get(id=id)
    context = {'processformkargars':karger.processformkargar_set.all()}
    return render(request, 'printReservesByOneKargar.html', context=context)


def printReserveFormsInOneProcess(request, id):
    process = Process.objects.get(id=id)
    context = {'forms':process.reserveform_set}
    return render(request, 'printReservesInOneProcess.html', context=context)





