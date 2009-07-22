from django.shortcuts import render_to_response
from django.template import RequestContext

def index(request):
    page_title = 'E-Commerce Enterprise Solutions'
    return render_to_response("truesite/index.html", locals(), RequestContext(request))

def design(request):
    page_title = 'E-Commerce Design'
    return render_to_response("truesite/design.html", locals(), RequestContext(request))

def integration(request):
    page_title = 'E-Commerce Integration'
    return render_to_response("truesite/integration.html", locals(), RequestContext(request))

def marketing(request):
    page_title = 'E-Commerce Marketing Solutions'
    return render_to_response("truesite/marketing.html", locals(), RequestContext(request))

def contact(request):
    page_title = 'Contact Us'
    return render_to_response("truesite/contact.html", locals(), RequestContext(request))
