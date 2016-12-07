from .models import Customer

from django import forms


class ProfileForm(forms.Form):
    name = forms.CharField(max_length=100, label='نام', required=False)
    email = forms.EmailField(label='ایمیل', required=False)

    def save(self, customer:Customer):
        user = customer.user
        if self.cleaned_data.get('email') != '':
            print('in email if')
            customer.email = self.cleaned_data['email']
            user.email = self.cleaned_data['email']
        if self.cleaned_data.get('name') != '':
            customer.name = self.cleaned_data['name']
        user.save()
        customer.save()









