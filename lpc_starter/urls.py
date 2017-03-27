"""lpc_starter URL Configuration
# -*- coding: utf-8 -*-
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

from evento.views import inicio, listaTipoAtividades, xTipoAtividade, listaAtividades, xAtividade, listaEventos

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', inicio, name='inicio'),
    url(r'^tipoatividades/', listaTipoAtividades, name='listaTipo'),
    url(r'^tipoatividadesx/([0-9])$', xTipoAtividade),
    url(r'^atividades/', listaAtividades, name='listaAtividade'),
    url(r'^atividadesx/([0-9])$', xAtividade),
    url(r'^eventos/', listaEventos, name='listaAEventos'),
    url(r'^eventosx/([0-9])$', xAtividade),

]
