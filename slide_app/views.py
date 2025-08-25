from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from django.core.exceptions import ObjectDoesNotExist
from django_twincat_http_server.utils import debug_printer
import django_twincat_http_server.settings as settings

def slide_home(request):
    printer = debug_printer(settings.DEBUG)
    match request.method:
        case "GET":
            slide_objects = Slide.objects.all().order_by('title')
            #slide_objects = sorted(slide_objects,key=lambda x : str(x))
            printer(slide_objects)
            context = {'slides':slide_objects}
            return render(request,'slide_home.html',context)
        case _:
            return HttpResponse(status=404)

def slide_page(request,slide_id=1):
    printer = debug_printer(settings.DEBUG)
    match request.method:
        case "GET":
            try:
                slide_object = Slide.objects.get(id=slide_id)
            except ObjectDoesNotExist as e:
                printer(e)
                return HttpResponse(status=404)
            #slide_objects = sorted(slide_objects,key=lambda x : str(x))
            printer(slide_object)
            context = {'slide':slide_object}
            return render(request,'slide_view.html',context)
        case _:
            return HttpResponse(status=404)
