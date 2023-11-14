from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.template import loader


def index(request):
    """ """
    treeview_data = {
        'a': {'a1': 'a1', 'a2': 'a2', 'a3': 'a3'},
        'b': {'b1': 'b1', 'b2': 'b2', 'b3': 'b3'},
        'c': {'c1': 'c1', 'c2': 'c2', 'c3': 'c3'},
        'd': 'd',
        'e': 'e',
        'f': 'f',
    }
    context = {'treeview_data': treeview_data}
    template = loader.get_template("mainframe/index.html")
    return HttpResponse(template.render(context, request))


