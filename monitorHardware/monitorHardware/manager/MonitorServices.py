import json
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime, timedelta
from ..models  import Services
import pickle
import os
import psutil

@csrf_exempt
def getAtTime(request):
    if request.method == "POST":
        return HttpResponse (
            json.dumps({'success': True}), 
            content_type="application/json",
        )
    if request.method == "GET":
        time = request.GET.get('timestamp','')
        if time:
            return getDataTime(time)
        else:
            return getLatest()
    else:
        return HttpResponse (
            json.dumps({'success': False}), 
            content_type="application/json",
        )

def getLatest():
    latestEntry = Services.objects.latest('pk')

    response_data = latestEntry.getResponseData()
    return HttpResponse(json.dumps(response_data), content_type="application/json")
    

def getDataTime(time):
    closestTimeEntry = getClosestObj(time)
    if closestTimeEntry == -1:
        return HttpResponse (
            json.dumps({'success': False}), 
            content_type="application/json",
        )
    entry = Services.objects.filter(timestamp = str(closestTimeEntry))
    response_data = entry[0].getResponseData()
    return HttpResponse(json.dumps(response_data), content_type="application/json")

def getClosestObj(time):
    print time
    time = datetime.fromtimestamp(float(time))
    times_greater = Services.objects.filter(timestamp__gt = time).order_by('timestamp')
    times_smaller = Services.objects.filter(timestamp__lt = time).order_by('-timestamp')
    # print times_greater
    try:
        try:
            closest_greater = times_greater[0]
        except:
            return times_smaller[0]
        try:
            closest_smaller = times_smaller[0]
        except:
            return times_greater[0]
    except:
        print "no objects"
        return -1
    if closest_greater - time > time - closest_smaller:
        return closest_greater
    else:
        return closest_smaller


def create_table_entry():
    curr = Services()
    curr.cpu_percent = psutil.cpu_times_percent()
    curr.cpu_count = psutil.cpu_count()
    curr.cpu_times = str(psutil.cpu_times())

    curr.mem_swap = psutil.swap_memory()
    curr.virtual_memory = psutil.virtual_memory()
    
    curr.disk_usage = psutil.disk_usage('/')
    curr.disk_io_counters = psutil.disk_io_counters()

    curr.save()

