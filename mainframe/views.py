from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.template import loader


def index(request):
    """ """
    treeview_data = {
        'a': {'a1': '/admin', 'a2': '/admin', 'a3': 'http://127.0.0.1:8000/admin'},
        'b': {'b1': 'http://134.134.34.71/browser/', 'b2': 'http://134.134.34.72/dc/nbrender/render/html/examples/cube_report.ipynb', 'b3': 'b3'},
        'c': {'c1': 'c1', 'c2': 'c2', 'c3': 'c3'},
        'd': 'http://127.0.0.1:8000/admin/login/?next=/admin/',
        'e': 'http://127.0.0.1:8000/static/mainframe/dist/img/user2-160x160.jpg',
        'f': 'f',
    }
    context = {'treeview_data': treeview_data}
    template = loader.get_template("mainframe/index.html")
    return HttpResponse(template.render(context, request))


