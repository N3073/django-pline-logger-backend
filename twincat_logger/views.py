from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt
from django_twincat_http_server.utils import debug_printer
import django_twincat_http_server.settings as settings
import json
from .models import *
def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[-1].strip()
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


@csrf_exempt
def tc_log(request,plineid=""):
    printer = debug_printer(settings.DEBUG)
    try:
        pline = ProductionLine.objects.get(id=plineid)
    except:
        return HttpResponse(status=404)
    ip = get_client_ip(request)
    match request.method:
        case "GET":
            data = {"args":{"message":"Hello TwinCAT!"}}
            #return HttpResponse("GET RESPONSE: Hello world!")
            #return HttpResponse(json.dumps(data), content_type='application/json')
            return JsonResponse(data)
        case "POST":
            incoming_data = json.loads(request.body)
            if "LOG_TYPE" in incoming_data:
                match incoming_data["LOG_TYPE"]:
                    case "MESSAGE":
                        
                        try:
                            message_entry = LogMessage(production_line=pline,message_type=incoming_data["message_type"],message_text=incoming_data["message_text"],sender_ip=ip)
                            message_entry.full_clean()
                            message_entry.save()
                            printer(str(message_entry))
                            return HttpResponse(status=204)
                        except Exception as e:
                            #print(e.message)
                            return HttpResponse(status=404)
                    case "DATA":
                        
                        try:
                            time_now=timezone.now()
                            for key in incoming_data['data']:
                            
                                data_entry = LogData(
                                    production_line=pline,
                                    data_name=key,
                                    data_field=float(incoming_data['data'][key]),
                                    time_of_creation=time_now,
                                    sender_ip=ip
                                    
                                    )
                                printer(str(data_entry))
                                data_entry.full_clean()
                                data_entry.save()
                            return HttpResponse(status=204)
                        except Exception as e:
                            #print(e.message)
                            return HttpResponse(status=404)
                    case _:
                        return HttpResponse(status=404)
        

    return HttpResponse(status=404)

def home_view(request):

    return render(request,"home.html")
