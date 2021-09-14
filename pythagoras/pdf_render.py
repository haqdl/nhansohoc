
import os
from django.conf import settings
from io import StringIO
from django.http import HttpResponse
from django.template.loader import get_template
import xhtml2pdf.pisa as pisa
from django.contrib.staticfiles import finders
from pprint import pprint
def link_callback(uri, rel):
        """
        Convert HTML URIs to absolute system paths so xhtml2pdf can access those
        resources
        """
        result = finders.find(uri)
        if result:
                if not isinstance(result, (list, tuple)):
                        result = [result]
                result = list(os.path.realpath(path) for path in result)
                path=result[0]
        else:
                sUrl = settings.STATIC_URL        # Typically /static/
                sRoot = settings.STATIC_ROOT      # Typically /home/userX/project_static/
                mUrl = settings.MEDIA_URL         # Typically /media/
                mRoot = settings.MEDIA_ROOT       # Typically /home/userX/project_static/media/

                if uri.startswith(mUrl):
                        path = os.path.join(mRoot, uri.replace(mUrl, ""))
                elif uri.startswith(sUrl):
                        path = os.path.join(sRoot, uri.replace(sUrl, ""))
                else:
                        return uri

        # make sure that file exists
        if not os.path.isfile(path):
                raise Exception(
                        'media URI must start with %s or %s' % (sUrl, mUrl)
                )
        return path


def render(path: str, params: dict):
    template = get_template(path)
    html = template.render(params)
    response =  StringIO()
    options = {'encoding': "UTF-8"}
    print(type(html))
    pdf = pisa.pisaDocument(html, response, encoding='UTF-8')
    if not pdf.err:
        return HttpResponse(response.getvalue(), content_type='application/pdf')
    else:
        return HttpResponse("Error Rendering PDF", status=400)


def render_pdf_view(path: str, params: dict):

    template = get_template(path)
    html = template.render(params)
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    # download
    response['Content-Disposition'] = "'attachment; filename='report.pdf'"
    # display
#     response['Content-Disposition'] = "filename='report.pdf'"
    # find the template and render it.

    template = get_template(path)

    html = template.render(params) 
    
    # create a pdf
    pisa_status = pisa.CreatePDF(html, dest=response, link_callback=link_callback, debug=1)
    
#     return HttpResponse('HERE')   
    # if error then show some funy view
    if pisa_status.err:
        return HttpResponse('We had some errors <pre>' + html + '</pre>')
    
    return HttpResponse(response.getvalue(), content_type='application/pdf')
#     return response
