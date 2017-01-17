"""love_eat URL Configuration

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
from django.conf.urls import url
from django.contrib import admin
from django.views.static import serve
from django import views

import t_reg_login.views
from love_eat import settings

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', t_reg_login.views.t_index_view),
    url(r'^index.html$', t_reg_login.views.t_index_view),
    url(r'^reg.html$', t_reg_login.views.t_reg_view),
    url(r'^login.html$', t_reg_login.views.t_login_view),
    url(r'^gen_yzm$', t_reg_login.views.gen_yzm),
    url(r'^family_reg$', t_reg_login.views.t_family_reg_func),
    url(r'^family_login$', t_reg_login.views.t_family_login_func),
]
