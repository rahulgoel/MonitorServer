python manage.py syncdb --noinitial-data
python manage.py runserver


This will start the server and the server adds a new entry to the database every 10 seconds for now. As along as the server is running the entries will keep getting appended to the end of the table. There is no deletion policy for now. So running this forever will give a memory error when the disk space runs out. I could limit the size or this might be a monitoring tool which may run only when required, so I didn't take a decision on that. 

the api's which are available are: 

/query/   [GET]

will return the latest system status (GET)

/querytime?timestamp=epoch will return the entry closest to the UNIX epoch specified
eg: /querytime?timestamp=1455490926

The data returned is: 
Timestamp, cpu_Data, memory_data, disk_data

I basically return data in string format by making calls to psutil library in python. 
The entries are: 
"cpu_percent": cpu_times_percent()
"cpu_count": cpu_count
"cpu_times": cpu_times
"mem_swap": swap_memory()
"mem_virtual": virtual_memory()
"disk_usage": disk_usage()
"disk_io": disk_io_counters()

Let me know if there are any questions

PS: Do not delete the sqlite3 database, use the syncdb command to initalize it as an empty database.
