# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt, csrf_protect, ensure_csrf_cookie
from django.views.decorators.csrf import ensure_csrf_cookie

from .models import TipoAtividade
from .models import Atividade
from .models import Evento


def inicio(request):
    html = """<h1>Opções</h1>
                <ul>
                    <li><a href='/eventos'>Eventos</a></li>
                    <li><a href='/atividades'>Atividades</a></li>
                    <li><a href='/tipoatividades'>Tipo de Atividades</a></li>
                </ul>
            """
    return HttpResponse(html)


"""Listando todos os Eventos"""
def listaEventos(request):
    html = "<h1>Lista de Eventos </h1>"
    lista = Evento.objects.all()
    for e in lista:
        html += '<li>Evento: {} </br>Local: {} </br>Início: {} </br> Fim: : {} </br>Início Inscrição: {} </br>Fim Inscrição: {} <br> Limite Incrições: {} <br> Apresentação: {} <br> Publico Alvo: {} <br> Programação: {} <br> Data Cadastro: {}</li></br></br>'.format(
            e.nome, e.local, e.abertura_evento, e.encerramento_evento, e.abertura_inscricoes, e.encerramento_inscricoes, e.limite_inscricoes, e.apresentacao, e.publico_alvo, e.programacao, e.data_cadastro)
    
    return HttpResponse(html)


"""Listando tEvento por parametro ID"""
def xEventos(request, id):
    html = "<h1>Tipo de Atividades por ID</h1>"
    e = Evento.objects.get(id=id)
    html += '<li>Evento: {} </br>Local: {} </br>Início: {} </br> Fim: : {} </br>Início Inscrição: {} </br>Fim Inscrição: {} <br> Limite Incrições: {} <br> Apresentação: {} <br> Publico Alvo: {} <br> Programação: {} <br> Data Cadastro: {}</li></br></br>'.format(
            e.nome, e.local, e.abertura_evento, e.encerramento_evento, e.abertura_inscricoes, e.encerramento_inscricoes, e.limite_inscricoes, e.apresentacao, e.publico_alvo, e.programacao, e.data_cadastro)
    
    return HttpResponse(html)


"""Listando todos os tipos de atividades"""
def listaTipoAtividades(request):
    html = "<h1>Lista de Tipo de Atividades</h1>"
    lista = TipoAtividade.objects.all()
    for tipo in lista:
        html += '<li>Tipo de Atividade: {} </br>Data Cadastro: {} </br></br></li>'.format(tipo.descricao, tipo.data_cadastro)
    
    return HttpResponse(html)


"""Listando tipo de atividade por parametro ID"""
def xTipoAtividade(request, id):
    html = "<h1>Tipo de Atividades por ID</h1>"
    t_atividade = TipoAtividade.objects.get(id=id)
    html += '<li>Tipo de Atividade: {} </br>Data Cadastro: {} </br></br></li>'.format(t_atividade.descricao, t_atividade.data_cadastro)
    
    return HttpResponse(html)


"""Listando todas as Atividades"""
def listaAtividades(request):
    html = "<h1>Lista de  Atividades</h1>"
    lista = Atividade.objects.all()
    for tipo in lista:
        html += '<li>Evento: {} </br>Tipo Atividade: {} </br>Tema: {} </br> Descrição: : {} </br>Início: {} </br>Fim: {} <br> Local: {}</li></br></br>'.format(
            tipo.evento, tipo.tipo_atividade, tipo.tema, tipo.descricao, tipo.abertura_atividade, tipo.encerramento_atividade, tipo.local)
    
    return HttpResponse(html)

"""Listando Atividade por parametro ID"""
def xAtividade(request, id):
    html = "<h1>Atividades por ID</h1>"
    x = Atividade.objects.get(id=id)
    html += '<li>Evento: {} </br>Tipo Atividade: {} </br>Tema: {} </br> Descrição: : {} </br>Início: {} </br>Fim: {} <br> Local: {}</li></br></br>'.format(
            x.evento, x.tipo_atividade, x.tema, x.descricao, x.abertura_atividade, x.encerramento_atividade, x.local)
    
    return HttpResponse(html)

