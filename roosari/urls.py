"""roosari URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from . import settings

from django.conf.urls import url, include
from django.contrib import admin
from django.conf.urls.static import static
from django.core.urlresolvers import reverse
from django.views.generic.base import RedirectView


urlpatterns = [
    url(r'^reserve/', include('ReserveForm.urls')),
    url(r'^user/', include('UserManager.urls')),
    url(r'^siteadmin/$', RedirectView.as_view(url='/reserve/siteadmin'), name='site'),
    url(r'^$', RedirectView.as_view(url='/admin'), name='AdminIndex'),
    url(r'^admin/', admin.site.urls),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
