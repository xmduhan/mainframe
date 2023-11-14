from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.template import loader


def index(request):
    """ """
    context = {}
    template = loader.get_template("mainframe/index.html")
    return HttpResponse(template.render(context, request))


