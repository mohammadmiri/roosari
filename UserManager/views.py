from ReserveForm.models import ReserveForm
from .models import Customer, CustomerMessage

from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, reverse
from django.core.mail import send_mail


import traceback


def loginFunc(request):
    error = ''
    if request.method == 'POST':
        try:
            email = request.POST['email']
            user = User.objects.get(email=email)
            password = request.POST['password']
            user = authenticate(username=user.username, password=password)
            if user is not None:
                login(request, user)
                return redirect(reverse('HomepageCustomer'))
            else:
                error = 'نام کاربری یا رمز اشتباه است'
        except User.DoesNotExist:
            error = 'نام کاربری یا رمز اشتباه است'
    context = {'error': error}
    return render(request, 'login.html', context)



def forget_password(request):
    error = ''
    if request.method == 'POST':
        email_to_send = request.POST['email']
        user = User.objects.filter(email=email_to_send).first()
        if user != None:
            fromMy = 'mirisitedeveloper@gmail.com'
            subj = 'تغییر رمز'
            message = ''
            html_message = '<html><body><p>' + \
                           'برای تغییر رمز خود برروی لینک زیر کلیک کنید' + \
                           '</p><p>' + \
                           '<a href=http://108.61.200.118:8000' + reverse('ResetPassword', args=[user.id]) + '>' + \
                           'اینجا' + \
                           '</a></p></body></html>'
            try:
                send_mail(subject=subj,
                          from_email=fromMy,
                          message=message,
                          recipient_list=[email_to_send, ],
                          html_message=html_message)
            except:
                error = 'امکان ارسال ایمیل وجود ندارد'
        else:
            error = 'ایمیل در سایت وجود ندارد'
    context = {'error': error}
    return render(request, 'forgetPassword.html', context)




def reset_password(request, id):
    error = ''
    if request.method == 'POST':
        password = request.POST['password']
        if len(password) < 8:
            error = 'رمز کمتر از ۸ کاراکتر است'
        else:
            user = User.objects.get(id=id)
            if user != None:
                user.set_password(password)
    context = {'error': error, 'id': id}
    return render(request, 'resetPassword.html', context)


def show_message(request, message):
    pass


@login_required()
def show_profile(request):
    customer = Customer.objects.get(user=request.user)
    context = {'customer':customer}
    return render(request, 'showProfileCustomer.html', context=context)


@login_required()
def homepage(request):
    customer = Customer.objects.get(user=request.user)
    context = {'customer':customer}
    return render(request, 'customerHomepage.html', context=context)



@login_required()
def show_reserves(request):
    customer = Customer.objects.get(user=request.user)
    forms = ReserveForm.objects.filter(customer=customer)
    context = {'forms':forms, 'customer':customer}
    return render(request, 'showReserves.html', context=context)



@login_required()
def show_event(request):
    customer = Customer.objects.get(user=request.user)
    context = {'customer':customer}
    return render(request, 'showEvents.html', context=context)


@login_required()
def exit(request):
    if request.user.is_authenticated():
        logout(request)
    else:
        return redirect(reverse('HomepageCustomer'))


@login_required()
def contact_us(request):
    if request.method == 'POST':
        message = request.POST['message']
        customerMessage = CustomerMessage.objects.create()
        customerMessage.message = message
        customerMessage.save()
        return redirect(reverse('HomepageCustomer'))
    return render(request, 'contactUs.html')

