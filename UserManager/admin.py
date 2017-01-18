from .models import Kargar, Customer, KarbarKarkhane, KarbarTehran, Event, AdminSite

from django.contrib import admin
from django.contrib.auth.models import User, Group
from django.db import models, IntegrityError, transaction
from django import forms
from django.contrib import messages
from django.core.exceptions import ValidationError

class EventInline(admin.TabularInline):
    model = Event
    extra = 1


class CustomerAdminForm(forms.ModelForm):
    class Meta:
        model = Customer
        exclude = ('user',)

    def clean_username(self):
        username = self.cleaned_data.get('username')
        try:
            user = User.objects.get(username=username)
            raise forms.ValidationError('نام کاربری تکراری است')
        except User.DoesNotExist:
            return username

class CustomerAdmin(admin.ModelAdmin):
    list_display = ('id', 'get_username', 'get_first_name', 'phoneNumber',)
    list_display_links = ('get_username',)
    search_fields = ('username', 'id', 'name')
    raw_id_fields = ('user',)
    inlines = [EventInline]
    exclude = ['user']
    form = CustomerAdminForm

    def get_username(self, obj):
        if obj.user.username is None:
            return '-'
        return obj.user.username
    get_username.__name__ = 'نام کاربری'

    def get_first_name(self, obj):
        if obj.name is None:
            return '-'
        return obj.name
    get_first_name.__name__ = 'نام'

    def save_model(self, request, obj, form, change):
        if change == False:
            user = User.objects.create_user(username=form.cleaned_data['username'], password=12345678,
                                            email=form.cleaned_data['email'])
            obj.user = user
            obj.save()
        else:
            if 'username' in form.cleaned_data or 'email' in form.cleaned_data:
                user = obj.user
                user.username = form.cleaned_data['username']
                user.email = form.cleaned_data['email']
                user.save()
            obj.save()

    formfield_overrides = {
        models.TextField: {'widget': forms.Textarea(attrs={'rows':1, 'cols':32})},
    }




class KargarAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_display_links = ('name',)



class KarbarTehranAdminForm(forms.ModelForm):
    class Meta:
        model = KarbarTehran
        exclude = ('user',)

    def clean_username(self):
        username = self.cleaned_data.get('username')
        try:
            user = User.objects.get(username=username)
            raise forms.ValidationError('نام کاربری تکراری است')
        except User.DoesNotExist:
            return username

class KarbarTehranAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'name')
    list_display_links = ('id', 'username', 'name')
    form = KarbarTehranAdminForm

    def get_readonly_fields(self, request, obj=None):
        groupnames = request.user.groups.values_list('name', flat=True)
        if 'karbarTehran' in groupnames:
            return ('username', 'email',)
        elif 'admin' in groupnames:
            return ()

    def save_model(self, request, obj, form, change):
        if change == False:
            user = User.objects.create_user(username=form.cleaned_data['username'], password=form.cleaned_data['password'],
                                            email = form.cleaned_data['email'], first_name = form.cleaned_data['name'])
            obj.user = user
            user.is_staff = True
            user.save()
            obj.save()
            group = Group.objects.get(name='karbarTehran')
            group.user_set.add(user)
        else:
            if 'username' in form.cleaned_data:
                obj.user.username = form.cleaned_data['username']
                obj.username = form.cleaned_data['username']
            if 'name' in form.cleaned_data:
                obj.user.first_name = form.cleaned_data['name']
                obj.name = form.cleaned_data['name']
            if 'password' in form.cleaned_data:
                obj.user.set_password(form.cleaned_data['password'])
                obj.password = form.cleaned_data['password']
            obj.user.save()
            obj.save()


class KarbarKarkhaneAdminForm(forms.ModelForm):
    class Meta:
        model = KarbarKarkhane
        exclude = ('user',)

    def clean_username(self):
        username = self.cleaned_data.get('username')
        try:
            user = User.objects.get(username=username)
            raise forms.ValidationError('نام کاربری تکراری است')
        except User.DoesNotExist:
            return username

class KarbarKarkhaneAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'name')
    list_display_links = ('id', 'username', 'name')
    form = KarbarKarkhaneAdminForm

    def get_readonly_fields(self, request, obj=None):
        groupnames = request.user.groups.values_list('name', flat=True)
        if 'karbarKarkhane' in groupnames:
            return ('username', 'email',)
        elif 'admin' in groupnames:
            return ()

    def save_model(self, request, obj, form, change):
        if change == False:
            user = User.objects.create_user(username=form.cleaned_data['username'], password=form.cleaned_data['password'],
                                            email = form.cleaned_data['email'])
            obj.user = user
            user.is_staff = True
            user.save()
            obj.save()
            group = Group.objects.get(name='karbarKarkhane')
            group.user_set.add(user)
        else:
            if 'username' in form.cleaned_data:
                obj.user.username = form.cleaned_data['username']
                obj.username = form.cleaned_data['username']
            if 'name' in form.cleaned_data:
                obj.user.first_name = form.cleaned_data['name']
                obj.name = form.cleaned_data['name']
            if 'password' in form.cleaned_data:
                obj.user.set_password(form.cleaned_data['password'])
                obj.password = form.cleaned_data['password']
            obj.user.save()
            obj.save()



class AdminSiteAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'name')
    list_display_links = ('id', 'username', 'name')

    def get_readonly_fields(self, request, obj=None):
        groupnames = request.user.groups.values_list('name', flat=True)
        if 'admin' in groupnames:
            return ('username',)
        return ()

    def get_form(self, request, obj=None, **kwargs):
        groupnames = request.user.groups.values_list('name', flat=True)
        if 'admin' in groupnames:
            self.exclude = ("user",)
        form = super(AdminSiteAdmin, self).get_form(request, obj, **kwargs)
        return form

    def save_model(self, request, obj, form, change):
        if change is True:
            if 'username' in form.cleaned_data:
                obj.user.username = form.cleaned_data['username']
                obj.username = form.cleaned_data['username']
            if 'name' in form.cleaned_data:
                obj.user.first_name = form.cleaned_data['name']
                obj.name = form.cleaned_data['name']
            if 'password' in form.cleaned_data:
                obj.user.set_password(form.cleaned_data['password'])
                obj.password = form.cleaned_data['password']
            obj.user.save()
            obj.save()



admin.site.register(AdminSite, AdminSiteAdmin)
admin.site.register(Customer, CustomerAdmin)
admin.site.register(Kargar, KargarAdmin)
admin.site.register(KarbarTehran, KarbarTehranAdmin)
admin.site.register(KarbarKarkhane, KarbarKarkhaneAdmin)








