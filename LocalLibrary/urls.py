from django.contrib import admin
from django.urls import include
from django.urls import path
from django.views.generic import RedirectView


urlpatterns = ([
    path('admin/', admin.site.urls),
    path('catalog/', include('catalog.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', RedirectView.as_view(url='/catalog', permanent=True))])
