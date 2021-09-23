
import os
from django.conf import settings
from io import StringIO, BytesIO
from django.http import HttpResponse
from django.template.loader import get_template, render_to_string
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
    result =  BytesIO()
    options = {'encoding': "UTF-8"}

    pdf = pisa.pisaDocument(BytesIO(html.encode("UTF-8")), result)
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
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


def render_wkhtml(path: str, params: dict):
    from wkhtmltopdf.views import PDFTemplateResponse

    template = get_template(path)
    html = template.render(params)

    response = PDFTemplateResponse(request=params['request'],
                                   template=path,
                                   filename="hello.pdf",
                                   context= params,
                                   show_content_in_browser=True,
                                   cmd_options={'margin-top': 50,},
                                   )
    return response

def render_pdfkit(path: str, params: dict):
    import pdfkit

    
    template = get_template(path)

    html = template.render(params) 
    options = {
        'page-size': 'Letter',
        'encoding': "UTF-8",
    }
    pdf = pdfkit.from_url("http://localhost:8000/", options)
    response = HttpResponse(pdf, content_type='application/pdf')
    response['Content-Disposition'] = "'attachment; filename='report.pdf'"
    return response      