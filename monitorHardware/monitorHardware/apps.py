from django.apps import AppConfig
import time,threading
from manager import MonitorServices

class MyAppConfig(AppConfig):
    name = 'monitorHardware'
    verbose_name = "Hardware Monitor"
    # time = 200

    def ready(self):
        print(time.ctime())
        MonitorServices.create_table_entry()
        threading.Timer(10, self.ready).start()
        print "here"
        # pass
