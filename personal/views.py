#encoding:utf-8
from django.shortcuts import render
from django.template import RequestContext
from django.template.loader import render_to_string
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.contrib import messages
from django.core.mail import EmailMultiAlternatives
from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import get_object_or_404

from django.contrib.auth.models import User

from scaincos.reportes import generar_pdf
from scaincos.log_usuarios import log_addition, log_change
from usuarios.models import Persona, Administrativo, Estudiante, Docente
from personal.form import PersonaForm, AdministrativoForm, EstudianteForm, DocenteForm

import random


def password_create():
    li = ['Q','W','E','R','T','Y','U','I','O','P','A','S','D','F','G','H','J','K','L','Z','X','C','V','B','N','M','1','2','3','4','5','6','7','8','9','0']
    #51 elementos
    code = random.choice(li)
    for i in range(5):
        code += random.choice(li)
    return code

@permission_required('usuarios.index_administrativo', login_url='/login')
def index_administrativo(request):
    administrativos = Administrativo.objects.all()
    log_change(request, request.user, 'Visita Index Administrativos')
    return render(request, 'administrativos/index.html', {
        'administrativos':administrativos,
    })

@permission_required('usuarios.add_administrativo', login_url='/login')
def new_administrativo(request):
    if request.method == 'POST':
        perform = PersonaForm(request.POST, request.FILES)
        admform = AdministrativoForm(request.POST)
        if perform.is_valid() and admform.is_valid():
            password = password_create()
            p = perform.save()
            u = User.objects.create_user(str(p.ci), p.email, password)
            p.usuario = u
            p.tipo = 'Administrativo'
            p.save()
            a = admform.save()
            a.persona = p
            a.save()
            u.email = p.email
            u.first_name = p.nombre
            u.last_name = p.paterno + ' ' + p.materno
            u.save()
            log_addition(request, p, 'Persona Creada')
            log_addition(request, u, 'Usuario Creado')
            log_addition(request, a, 'Administrador Creado')
            html = render_to_string('administrativos/email_confimacion.html',{
                'username':u.username,
                'password':password,
            }, context_instance=RequestContext(request))
            subject = 'Cuenta Creada Correctamente'
            text_content = 'Mensaje...nLinea 2nLinea3'
            html_content = html
            from_email = '"INCOS" <sieboliva@gmail.com>'
            to = p.email
            msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
            msg.attach_alternative(html_content, "text/html")
            msg.send()
            sms = "Administratico Creado Correctamente"
            messages.success(request, sms)
            sms = "Un mensaje fue enviado a <strong>%s</strong> con los datos de su Cuenta"% (p.email)
            messages.success(request, sms)
            return HttpResponseRedirect(reverse(index_administrativo))
    else:
        perform = PersonaForm()
        admform = AdministrativoForm()
    return render(request, 'administrativos/new.html', {
        'perform':perform,
        'admform':admform,
    })

@permission_required('usuarios.report_administrativo', login_url='/login')
def pdf_administrativos(request):
    log_change(request, request.user, 'Reporte Pdf Administrativos')
    administrativos = Administrativo.objects.all()
    html = render_to_string('administrativos/pdf_administrativos.html', {
        'pagesize':'letter',
        'administrativos':administrativos,
    }, context_instance=RequestContext(request))
    return generar_pdf(html)

@permission_required('usuarios.change_administrativo', login_url='/login')
def change_administrativo(request):
    administrativos = Administrativo.objects.all()
    return render(request, 'administrativos/change.html', {
        'administrativos':administrativos,
    })

@permission_required('usuarios.change_administrativo', login_url='/login')
def update_administrativo(request, persona_id):
    persona = get_object_or_404(Persona, pk = persona_id)
    adm = Administrativo.objects.get(persona_id = persona.id)
    if request.method == 'POST':
        perform = PersonaForm(request.POST, request.FILES, instance=persona)
        admform = AdministrativoForm(request.POST, instance=adm)
        if perform.is_valid() and admform.is_valid():
            p = perform.save()
            a = admform.save()
            log_change(request, p, 'Persona Modificada')
            log_change(request, a, 'Persona Modificada')
            sms = "Administratico <strong>%s %s, %s</strong> Modificado Correctamente"%(p.paterno, p.materno, p.nombre)
            messages.success(request, sms)
            return HttpResponseRedirect(reverse(index_administrativo))
    else:
        perform = PersonaForm(instance=persona)
        admform = AdministrativoForm(instance=adm)
    return  render(request, 'administrativos/update.html', {
        'perform':perform,
        'admform':admform,
    })

@permission_required('usuarios.detail_administrativo', login_url='/login')
def list_detail_administrativo(request):
    administrativos = Administrativo.objects.all()
    return render(request, 'administrativos/list_detail.html', {
        'administrativos':administrativos,
    })

@permission_required('usuarios.detail_administrativo', login_url='/login')
def detail_administrativo(request, id_adm):
    adm = get_object_or_404(Administrativo, pk = id_adm)
    return render(request, 'administrativos/detail.html',{
        'adm':adm,
    })

@permission_required('usuarios.index_estudiante', login_url='/login')
def index_estudiantes(request):
    estudiantes = Estudiante.objects.all()
    return render(request, 'estudiante/index.html', {
        'estudiantes':estudiantes,
    })

@permission_required('usuarios.add_estudiante', login_url='/login')
def new_estudiante(request):
    if request.method == 'POST':
        perform = PersonaForm(request.POST, request.FILES)
        estform = EstudianteForm(request.POST)
        if perform.is_valid() and estform.is_valid():
            password = password_create()
            p = perform.save()
            u = User.objects.create_user(str(p.ci), p.email, password)
            p.usuario = u
            p.tipo = 'Estudiante'
            p.save()
            e = estform.save()
            e.persona = p
            e.save()
            u.email = p.email
            u.first_name = p.nombre
            u.last_name = p.paterno + ' ' + p.materno
            u.save()
            log_addition(request, p, 'Persona Creada')
            log_addition(request, u, 'Usuario Creado')
            log_addition(request, e, 'Estudiante Creado')
            html = render_to_string('estudiante/email_confimacion.html',{
                'username':u.username,
                'password':password,
            }, context_instance=RequestContext(request))
            subject = 'Cuenta Creada Correctamente'
            text_content = 'Mensaje...nLinea 2nLinea3'
            html_content = html
            from_email = '"INCOS" <sieboliva@gmail.com>'
            to = p.email
            msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
            msg.attach_alternative(html_content, "text/html")
            msg.send()
            sms = "Estudiante Creado Correctamente"
            messages.success(request, sms)
            sms = "Un mensaje fue enviado a <strong>%s</strong> con los datos de su Cuenta"% (p.email)
            messages.success(request, sms)
            return HttpResponseRedirect(reverse(index_estudiantes))
    else:
        perform = PersonaForm()
        estform = EstudianteForm()
    return render(request, 'estudiante/new.html', {
        'perform':perform,
        'estform':estform,
    })

@permission_required('usuarios.change_estudiante', login_url='/login')
def change_estudiante(request):
    estudiantes = Estudiante.objects.all()
    return render(request, 'estudiante/list_change.html', {
        'estudiantes':estudiantes,
    })

@permission_required('usuarios.change_estudiante', login_url='/login')
def update_estudiante(request, est_id):
    est = get_object_or_404(Estudiante, pk = est_id)
    per = Persona.objects.get(pk = est.persona_id)
    if request.method == 'POST':
        perform = PersonaForm(request.POST, request.FILES, instance=per)
        estform = EstudianteForm(request.POST, instance=est)
        if estform.is_valid() and perform.is_valid():
            p = perform.save()
            a = estform.save()
            log_change(request, p, 'Persona Modificada')
            log_change(request, a, 'Estudiante Modificado')
            sms = "Estudiante <strong>%s %s, %s</strong> Modificado Correctamente"%(p.paterno, p.materno, p.nombre)
            messages.success(request, sms)
            return HttpResponseRedirect(reverse(index_estudiantes))
    else:
        perform = PersonaForm(instance=per)
        estform = EstudianteForm(instance=est)
    return render(request, 'estudiante/update.html', {
        'perform':perform,
        'estform':estform,
    })

@permission_required('usuarios.detail_estudiante', login_url='/login')
def list_detail_estudiante(request):
    estudiantes = Estudiante.objects.all()
    return render(request, 'estudiante/list_detail.html', {
        'estudiantes':estudiantes,
    })

@permission_required('usuarios.detail_estudiante', login_url='/login')
def detail_estudiante(request, est_id):
    estudiante = get_object_or_404(Estudiante, pk = est_id)
    return render(request, 'estudiante/detail.html', {
        'estudiante':estudiante,
    })

@permission_required('usuarios.report_estudiante', login_url='/login')
def pdf_estudianes(request):
    estudiantes = Estudiante.objects.filter(persona__activo = True)
    html = render_to_string('estudiante/pdf_estudiantes.html', {
        'estudiantes':estudiantes,
    }, context_instance=RequestContext(request))
    return generar_pdf(html)

@permission_required('usuarios.index_docente', login_url='/login')
def index_docente(request):
    docentes = Docente.objects.all()
    return render(request, 'docentes/index.html', {
        'docentes':docentes,
    })

@permission_required('usuarios.add_docente', login_url='/login')
def new_docente(request):
    if request.method == 'POST':
        perform = PersonaForm(request.POST, request.FILES)
        docform = DocenteForm(request.POST)
        if perform.is_valid() and docform.is_valid() :
            password = password_create()
            p = perform.save()
            u = User.objects.create_user(str(p.ci), p.email, password)
            p.usuario = u
            p.tipo = 'Docente'
            p.save()
            d = docform.save()
            d.persona = p
            d.save()
            u.email = p.email
            u.first_name = p.nombre
            u.last_name = p.paterno + ' ' + p.materno
            u.save()
            log_addition(request, p, 'Persona Creada')
            log_addition(request, u, 'Usuario Creado')
            log_addition(request, d, 'Docente Creado')
            html = render_to_string('docentes/email_confimacion.html',{
                'username':u.username,
                'password':password,
            }, context_instance=RequestContext(request))
            subject = 'Cuenta Creada Correctamente'
            text_content = 'Mensaje...nLinea 2nLinea3'
            html_content = html
            from_email = '"INCOS" <sieboliva@gmail.com>'
            to = p.email
            msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
            msg.attach_alternative(html_content, "text/html")
            msg.send()
            sms = "Docente Creado Correctamente"
            messages.success(request, sms)
            sms = "Un mensaje fue enviado a <strong>%s</strong> con los datos de su Cuenta"% (p.email)
            messages.success(request, sms)
            return HttpResponseRedirect(reverse(index_docente))
    else:
        perform = PersonaForm()
        docform = DocenteForm()
    return render(request, 'docentes/new.html', {
        'perform':perform,
        'docform':docform,
    })

@permission_required('usuarions.change_docente', login_url='/login')
def change_docente(request):
    docentes = Docente.objects.all()
    return render(request, 'docentes/change.html', {
        'docentes':docentes,
    })

@permission_required('usuarios.change_docente', login_url='/login')
def update_docente(request, doc_id):
    docente = get_object_or_404(Docente, pk = doc_id)
    persona = get_object_or_404(Persona, pk = docente.persona_id)
    if request.method == 'POST':
        perform = PersonaForm(request.POST, request.FILES, instance=persona)
        docform = DocenteForm(request.POST, instance=docente)
        if perform.is_valid() and docform.is_valid():
            p = perform.save()
            d = docform.save()
            log_change(request, p, 'Persona Modificada')
            log_change(request, d, 'Docente Modificado')
            sms = "Docente <strong>%s %s, %s</strong> Modificado Correctamente"%(p.paterno, p.materno, p.nombre)
            messages.success(request, sms)
            return HttpResponseRedirect(reverse(index_docente))
    else:
        perform = PersonaForm(instance=persona)
        docform = DocenteForm(instance=docente)
    return render(request, 'docentes/update.html', {
        'perform':perform,
        'docform':docform,
    })

@permission_required('usuarios.detail_docente', login_url='/login')
def list_detail_docente(request):
    docentes = Docente.objects.all()
    return render(request, 'docentes/list_detail.html', {
        'docentes':docentes,
    })

@permission_required('usuarios.detail_docente', login_url='/login')
def detail_docente(request, doc_id):
    docente = get_object_or_404(Docente, pk = doc_id)
    return render(request, 'docentes/detail.html', {
        'docente':docente,
    })

@permission_required('usuarios.report_docente', login_url='/login')
def pdf_docentes(request):
    docentes = Docente.objects.all()
    html = render_to_string('docentes/pdf_docentes.html', {
        'docentes':docentes,
    }, context_instance=RequestContext(request))
    return generar_pdf(html)