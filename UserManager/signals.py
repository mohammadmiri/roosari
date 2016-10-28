from .models import Customer

from django.contrib.auth.models import User
from django.db.models.signals import pre_delete
from django.dispatch import receiver


@receiver(pre_delete)
def customer_pre_delete(sender, **kwargs):
    print('before delete')




pre_delete.connect(customer_pre_delete)