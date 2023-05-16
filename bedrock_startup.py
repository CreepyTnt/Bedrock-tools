import bedrock_tools as mc
from datetime import date
from datetime import datetime
import json
from win10toast import ToastNotifier
import time

options = mc.get_options()
print (options['backup_path'])
print (options['last_backup'])
print (options['days_between_backups'])

try:
    d0 = json.loads(options['last_backup'])
    d0 = date(d0[0], d0[1], d0[2])
except:
    d0 = date(2007, 8, 7)

d0 = date(d0.year, d0.month, d0.day)
now = datetime.now()
d1 = date(now.year, now.month, now.day)
delta = d1 - d0
print (delta.days)


# f = open("C:\Bedrock\last_backup.json", 'w')
# f.write(json.dumps([2023, 4, 30]))
# f.close()


toaster = ToastNotifier()

if delta.days > int(options['days_between_backups']):
    mc.backup_worlds(options['backup_path'])

    # Send a notification
    try:
        toaster.show_toast("Bedrock Launcher", "Minecraft words backup completed", duration=10)
    except:
        print('notification sent')
else:
    print ('not time for backup yet')


time.sleep(60)

