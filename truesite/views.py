from django.shortcuts import render_to_response
from django.template import RequestContext

def index(request):
    page_title = 'E-Commerce Enterprise Solutions - True Platform'
    return render_to_response("truesite/index.html", locals(), RequestContext(request))

def design(request):
    return render_to_response("truesite/design.html", locals(), RequestContext(request))

def integration(request):
    return render_to_response("truesite/integration.html", locals(), RequestContext(request))

def marketing(request):
    return render_to_response("truesite/marketing.html", locals(), RequestContext(request))

def contact(request):
    return render_to_response("truesite/contact.html", locals(), RequestContext(request))
