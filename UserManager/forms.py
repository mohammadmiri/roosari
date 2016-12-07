from .models import Customer

from django import forms


class ProfileForm(forms.Form):
    name = forms.CharField(max_length=100, label='نام',)
    email = forms.EmailField(label='ایمیل', required=False)

    def save(self, customer:Customer):
        customer.email = self.cleaned_data['email']
        customer.name = self.cleaned_data['name']
        user = customer.user
        user.email = self.cleaned_data['email']
        user.save()
        customer.save()









