#encoding:utf-8
from django.http import HttpResponse
from django.conf import settings
import ho.pisa as pisa
import cStringIO as StringIO
import cgi
import os

def generar_pdf(html):
    result = StringIO.StringIO()
    #links = lambda uri, rel: os.path.join(settings.MEDIA_ROOT, uri.replace(settings.MEDIA_URL, ''))

    pdf = pisa.pisaDocument(StringIO.StringIO(html.encode("utf-16")), dest=result, link_callback=fetch_resources)
    #pdf = pisa.pisaDocument(StringIO.StringIO(html.encode("UTF-8")), result)
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    return HttpResponse('Error al generar el PDF: %s' % cgi.escape(html))


def fetch_resources(uri, rel):
    import os.path
    BASE_DIR = settings.BASE_DIR
    path = os.path.join(
            os.path.join(BASE_DIR, 'static'),
            uri.replace(settings.STATIC_URL, ""))
    return path

from django.contrib import messages
def sms_sesion(request):
    if  request.session['gestion'] == None:
        sms = 'No Tiene Seleccionada Ninguna Gestion'
    else:
        sms = 'Usted Se Encuentra en la Gestion <strong>%s</strong>' %(request.session['gestion'])
    messages.info(request, sms)