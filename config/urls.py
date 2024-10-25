"""zipcodes URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.urls import path, include
from django.conf import settings
from django.contrib import admin
from django.shortcuts import redirect

urlpatterns = [
    path(F'admin/{settings.URL_SECRET_KEY}/', admin.site.urls),
    path('estados/', include('states.urls')),
    path('ciudades/', include('cities.urls')),
    path('colonias/', include('neighborhoods.urls')),
    path('postales/', include('postalcodes.urls')),
    path('paqueterias/', include('carriers.urls')),
    path('servicios/', include('services.urls')),
    path('coberturas/', include('postalconnectedservices.urls')),
    path('zonificacion/', include('zonification.urls')),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
