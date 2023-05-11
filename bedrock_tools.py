import os
import shutil
from datetime import datetime
import json
import getpass
import time


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

def import_pack(path):# .mcpack or .mcworld

    username = getpass.getuser()

    os.system (path)

def start_game(fov_changer = False):
    if fov_changer:
        try:
            os.system('"C:\Bedrock\FOV-Changer.exe"')
        except:
            print ('fov-changer is not installed')
    os.system('start minecraft://')

def read(path):
    f = open(path, 'r')
    fdata = f.read()
    f.close()
    return (fdata)

def get_world_info(folder):
    name = read('C:\\Users\\jenni\\AppData\\Local\\Packages\\Microsoft.MinecraftUWP_8wekyb3d8bbwe\\LocalState\\games\\com.mojang\\minecraftWorlds\\' + folder +'\\levelname.txt')
    resources = read('C:\\Users\\jenni\\AppData\\Local\\Packages\\Microsoft.MinecraftUWP_8wekyb3d8bbwe\\LocalState\\games\\com.mojang\\minecraftWorlds\\' + folder + '\\world_resource_packs.json')
    behaviors = read ('C:\\Users\\jenni\\AppData\\Local\\Packages\\Microsoft.MinecraftUWP_8wekyb3d8bbwe\\LocalState\\games\\com.mojang\\minecraftWorlds\\' + folder + '\\world_behavior_packs.json')
    path = 'C:\\Users\\jenni\\AppData\\Local\\Packages\\Microsoft.MinecraftUWP_8wekyb3d8bbwe\\LocalState\\games\\com.mojang\\minecraftWorlds\\' + folder

    info = {
        'name' : name,
        'resources' : resources,
        'behaviors' : behaviors,
        'path' : path
    }
    return info


def clear_pack_history(folder):
    try:
        os.remove('C:\\Users\\jenni\\AppData\\Local\\Packages\\Microsoft.MinecraftUWP_8wekyb3d8bbwe\\LocalState\\games\\com.mojang\\minecraftWorlds\\' + folder + '\\world_behavior_pack_history.json')
        os.remove('C:\\Users\\jenni\\AppData\\Local\\Packages\\Microsoft.MinecraftUWP_8wekyb3d8bbwe\\LocalState\\games\\com.mojang\\minecraftWorlds\\' + folder + '\\world_resource_pack_history.json')
        print('completed')
    except:
        print('completed')







def get_resource_pack_info():
    pack_list = []
    resource_packs_path = r'C:\Users\jenni\AppData\Local\Packages\Microsoft.MinecraftUWP_8wekyb3d8bbwe\LocalState\games\com.mojang\resource_packs'
    
    for pack_name in os.listdir(resource_packs_path):
        pack_folder_path = os.path.join(resource_packs_path, pack_name)
        manifest_path = os.path.join(pack_folder_path, 'manifest.json')

        if os.path.isdir(pack_folder_path) and os.path.isfile(manifest_path):
            with open(manifest_path, 'r') as f:
                try:
                    manifest_data = json.load(f)
                    pack_info = {
                        'name': manifest_data.get('header', {}).get('name', ''),
                        'uuid': manifest_data.get('header', {}).get('uuid', ''),
                        'description': manifest_data.get('header', {}).get('description', ''),
                        'version': manifest_data.get('header', {}).get('version', '')
                    }
                    pack_list.append(pack_info)
                except json.JSONDecodeError as e:
                    print(f"Error loading JSON in pack: {pack_name}. Error: {str(e)}")
        else:
            print(f"Invalid pack folder or manifest not found for pack: {pack_name}")

    return pack_list


def get_behavior_pack_info():
    pack_list = []
    behavior_packs_path = r'C:\Users\jenni\AppData\Local\Packages\Microsoft.MinecraftUWP_8wekyb3d8bbwe\LocalState\games\com.mojang\behavior_packs'
    
    for pack_name in os.listdir(behavior_packs_path):
        pack_folder_path = os.path.join(behavior_packs_path, pack_name)
        manifest_path = os.path.join(pack_folder_path, 'manifest.json')

        if os.path.isdir(pack_folder_path) and os.path.isfile(manifest_path):
            with open(manifest_path, 'r') as f:
                try:
                    manifest_data = json.load(f)
                    pack_info = {
                        'name': manifest_data.get('header', {}).get('name', ''),
                        'uuid': manifest_data.get('header', {}).get('uuid', ''),
                        'description': manifest_data.get('header', {}).get('description', ''),
                        'version': manifest_data.get('header', {}).get('version', '')
                    }
                    pack_list.append(pack_info)
                except json.JSONDecodeError as e:
                    print(f"Error loading JSON in pack: {pack_name}. Error: {str(e)}")
        else:
            print(f"Invalid pack folder or manifest not found for pack: {pack_name}")

    return pack_list



#backup_main(installpath)
#get_world_dict()
#print (world_dict['test'])
#backup_worlds(installpath)




