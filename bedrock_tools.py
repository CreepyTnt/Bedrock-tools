import os
import shutil
from datetime import datetime
import json



def get_options():
    f = open(r'C:\Bedrock\backup_location.txt', 'r')
    installpath = f.read()
    f.close()

    f = open(r'C:\Bedrock\last_backup.json', 'r')
    last_backup = f.read()
    f.close()

    f = open(r'C:\Bedrock\days_between_backups.txt', 'r')
    days = f.read()
    f.close()


    return{
        'backup_path' : installpath,
        'last_backup' : last_backup,
        'days_between_backups' : days
    }


world_dict = {
        'world_path': 'world_name'
    }
def get_world_dict():#creats a dictionary of all worlds
    for i in os.listdir(r'C:\Users\jenni\AppData\Local\Packages\Microsoft.MinecraftUWP_8wekyb3d8bbwe\LocalState\games\com.mojang\minecraftWorlds'):
        print(i)
        f = open(r'C:\\Users\\jenni\AppData\\Local\\Packages\\Microsoft.MinecraftUWP_8wekyb3d8bbwe\\LocalState\\games\\com.mojang\\minecraftWorlds\\' + i + r'\\' + r'levelname.txt', 'r' )
        content = f.read()
        world_dict[i] = content
        f.close()
    return (world_dict)

def backup_main(backup_path):
    print ('backup started')
    try:
        shutil.copytree(r'C:\Users\jenni\AppData\Local\Packages\Microsoft.MinecraftUWP_8wekyb3d8bbwe\LocalState\games\com.mojang', backup_path + '\\com.mojang')
    except:
        print ('backup already exsists')
        shutil.rmtree(backup_path + '\\com.mojang')
        shutil.copytree(r'C:\Users\jenni\AppData\Local\Packages\Microsoft.MinecraftUWP_8wekyb3d8bbwe\LocalState\games\com.mojang', backup_path + '\\com.mojang')
    f = open(r'C:\Bedrock\last_backup.json', 'w')
    f.write(json.dumps([datetime.now().year, datetime.now().month, datetime.now().day]))
    f.close()
    print ('backup finished')

def backup_worlds(backup_path):
    print ('starting backup')
    try:
        shutil.copytree(r'C:\Users\jenni\AppData\Local\Packages\Microsoft.MinecraftUWP_8wekyb3d8bbwe\LocalState\games\com.mojang\minecraftWorlds', backup_path + '\\com.mojang\\\minecraftWorlds')
    except:
        print ('backup already exsists')
        shutil.rmtree(backup_path + '\\com.mojang\\minecraftWorlds')
        shutil.copytree(r'C:\Users\jenni\AppData\Local\Packages\Microsoft.MinecraftUWP_8wekyb3d8bbwe\LocalState\games\com.mojang\minecraftWorlds', backup_path + '\\com.mojang\\\minecraftWorlds')
    f = open(r'C:\Bedrock\last_backup.json', 'w')
    f.write(json.dumps([datetime.now().year, datetime.now().month, datetime.now().day]))
    f.close()
    print ('backup finished')

def backup_settings(backup_path):
    print ('backup started')
    try:
        shutil.copytree(r'C:\Users\jenni\AppData\Local\Packages\Microsoft.MinecraftUWP_8wekyb3d8bbwe\LocalState\games\com.mojang\minecraftpe\options.txt', backup_path + '\\com.mojang\\options')
    except:
        print ('backup already exsists')
        shutil.rmtree(backup_path + '\\com.mojang\\options')
        shutil.copytree(r'C:\Users\jenni\AppData\Local\Packages\Microsoft.MinecraftUWP_8wekyb3d8bbwe\LocalState\games\com.mojang\minecraftpe\options.txt', backup_path + '\\com.mojang\\options')
    print ('backup finished')



#backup_main(installpath)
#get_world_dict()
#print (world_dict['test'])
#backup_worlds(installpath)
