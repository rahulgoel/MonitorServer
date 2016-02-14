from django.db import models
from datetime import datetime, timedelta
import time

class Services(models.Model):
    timestamp = models.DateTimeField(default=datetime.now())
    cpu_times = models.CharField(max_length=200)
    cpu_count = models.IntegerField(default = 0)
    cpu_percent = models.CharField(max_length=200)

    mem_virtual = models.CharField(max_length=200)
    mem_swap = models.CharField(max_length=200)

    disk_usage =  models.CharField(max_length=200)
    disk_io_counters =  models.CharField(max_length=200)

    
    def __unicode__(self):
        return u"%s" % (self.timestamp)

    def getResponseData(self):

        #Create Resposne Dictionary
        response_data = {}
        response_data["timestamp"] = str(self.timestamp)
        cpu_dict = {
            "cpu_times":self.cpu_times,
            "cpu_count":self.cpu_count,
            "cpu_percent":self.cpu_percent
        }
        mem_dict = {
            "mem_virtual":self.mem_virtual,
            "mem_swap":self.mem_swap
        }
        disk_dict = {
            "disk_usage":self.disk_usage,
            "disk_io_counters":self.disk_io_counters
        }

        response_data["values"] = {
            "cpu_dict":cpu_dict,
            "mem_dict":mem_dict,
            "disk_dict":disk_dict
        }
        return response_data
    
