import os
import shutil
from datetime import datetime
import json
import getpass
import time
import shutil
import zipfile

username = getpass.getuser()

def zip_folder(folder_path, zip_path):
    with zipfile.ZipFile(zip_path, 'w') as zipf:
        for root, _, files in os.walk(folder_path):
            for file in files:
                file_path = os.path.join(root, file)
                arcname = os.path.relpath(file_path, folder_path)
                zipf.write(file_path, arcname=arcname)


def get_options():
    f = open(f'C:\\Bedrock\\backup_location.txt', 'r')
    installpath = f.read()
    f.close()

    f = open(f'C:\\Bedrock\\last_backup.json', 'r')
    last_backup = f.read()
    f.close()

    f = open(f'C:\\Bedrock\\days_between_backups.txt', 'r')
    days = f.read()
    f.close()


    return{
        'backup_path' : installpath,
        'last_backup' : last_backup,
        'days_between_backups' : days
    }



def get_world_dict():#creats a dictionary of all worlds
    worlds = []

    for i in os.listdir(f'C:\\Users\\{username}\\AppData\\Local\\Packages\\Microsoft.MinecraftUWP_8wekyb3d8bbwe\\LocalState\\games\\com.mojang\\minecraftWorlds'):
        print(i)

        f = open(f'C:\\Users\\{username}\\AppData\\Local\\Packages\\Microsoft.MinecraftUWP_8wekyb3d8bbwe\\LocalState\\games\\com.mojang\\minecraftWorlds\\' + i + '\\' + 'levelname.txt', 'r' )
        content = f.read()
        world_dict = {
            'folder' : i,
            'name' : content
        }
        worlds.append(world_dict)
        f.close()


    return (worlds)

def backup_main(backup_path):
    print ('backup started')
    try:
        shutil.copytree(f'C:\\Users\\{username}\\AppData\\Local\\Packages\\Microsoft.MinecraftUWP_8wekyb3d8bbwe\\LocalState\\games\\com.mojang', backup_path + '\\com.mojang')
    except:
        print ('backup already exsists')
        shutil.rmtree(backup_path + '\\com.mojang')
        shutil.copytree(f'C:\\Users\\{username}\\AppData\\Local\\Packages\\Microsoft.MinecraftUWP_8wekyb3d8bbwe\\LocalState\\games\\com.mojang', backup_path + '\\com.mojang')
    f = open(f'C:\\Bedrock\\last_backup.json', 'w')
    f.write(json.dumps([datetime.now().year, datetime.now().month, datetime.now().day]))
    f.close()
    print ('backup finished')

def backup_worlds(backup_path):
    print ('starting backup')
    try:
        shutil.copytree(f'C:\\Users\\{username}\\AppData\\Local\\Packages\\Microsoft.MinecraftUWP_8wekyb3d8bbwe\\LocalState\\games\\com.mojang\\minecraftWorlds', backup_path + '\\com.mojang\\\minecraftWorlds')
    except:
        print ('backup already exsists')
        shutil.rmtree(backup_path + '\\com.mojang\\minecraftWorlds')
        shutil.copytree(f'C:\\Users\\{username}\\AppData\\Local\\Packages\\Microsoft.MinecraftUWP_8wekyb3d8bbwe\\LocalState\\games\\com.mojang\\minecraftWorlds', backup_path + '\\com.mojang\\\minecraftWorlds')
    f = open(f'C:\\Bedrock\\last_backup.json', 'w')
    f.write(json.dumps([datetime.now().year, datetime.now().month, datetime.now().day]))
    f.close()
    print ('backup finished')

def backup_settings(backup_path):
    print ('backup started')
    try:
        shutil.copytree(f'C:\\Users\\{username}\\AppData\\Local\\Packages\\Microsoft.MinecraftUWP_8wekyb3d8bbwe\\LocalState\\games\\com.mojang\\minecraftpe\\options.txt', backup_path + '\\com.mojang\\options')
    except:
        print ('backup already exsists')
        shutil.rmtree(backup_path + '\\com.mojang\\options')
        shutil.copytree(f'C:\\Users\\{username}\\AppData\\Local\\Packages\\Microsoft.MinecraftUWP_8wekyb3d8bbwe\\LocalState\\games\\com.mojang\\minecraftpe\\options.txt', backup_path + '\\com.mojang\\options')
    print ('backup finished')

def import_pack(path):# .mcpack or .mcworld


    os.system (path)

def start_game(fov_changer = False):
    if fov_changer:
        try:
            os.system(f'C:\\Bedrock\\FOV-Changer.exe')
        except:
            print ('fov-changer is not installed')
    os.system('start minecraft://')

def read(path):
    f = open(path, 'r')
    fdata = f.read()
    f.close()
    return (fdata)

def get_world_info(folder):

    name = read(f'C:\\Users\\{username}\\AppData\\Local\\Packages\\Microsoft.MinecraftUWP_8wekyb3d8bbwe\\LocalState\\games\\com.mojang\\minecraftWorlds\\' + folder +'\\levelname.txt')
    try:
        resources = read(f'C:\\Users\\{username}\\AppData\\Local\\Packages\\Microsoft.MinecraftUWP_8wekyb3d8bbwe\\LocalState\\games\\com.mojang\\minecraftWorlds\\' + folder + '\\world_resource_packs.json')
    except:
        resources = []
    try:
        behaviors = read (f'C:\\Bedrock\\AppData\\Local\\Packages\\Microsoft.MinecraftUWP_8wekyb3d8bbwe\\LocalState\\games\\com.mojang\\minecraftWorlds\\' + folder + '\\world_behavior_packs.json')
    except:
        behaviors = []

    path = f'C:\\Users\\{username}\\AppData\\Local\\Packages\\Microsoft.MinecraftUWP_8wekyb3d8bbwe\\LocalState\\games\\com.mojang\\minecraftWorlds\\' + folder

    info = {
        'name' : name,
        'resources' : resources,
        'behaviors' : behaviors,
        'path' : path
    }
    return info


def clear_pack_history(folder):
    try:
        os.remove(f'C:\\Users\\{username}\\AppData\\Local\\Packages\\Microsoft.MinecraftUWP_8wekyb3d8bbwe\\LocalState\\games\\com.mojang\\minecraftWorlds\\' + folder + '\\world_behavior_pack_history.json')
        os.remove(f'C:\\Users\\{username}\\AppData\\Local\\Packages\\Microsoft.MinecraftUWP_8wekyb3d8bbwe\\LocalState\\games\\com.mojang\\minecraftWorlds\\' + folder + '\\world_resource_pack_history.json')
        print('completed')
    except:
        print('completed')







def get_resource_pack_info():
    pack_list = []
    resource_packs_path = f'C:\\Users\\{username}\\AppData\\Local\\Packages\\Microsoft.MinecraftUWP_8wekyb3d8bbwe\\LocalState\\games\\com.mojang\\resource_packs'
    
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
                        'version': manifest_data.get('header', {}).get('version', ''),
                        'path' : pack_folder_path
                    }
                    pack_list.append(pack_info)
                except json.JSONDecodeError as e:
                    print(f"Error loading JSON in pack: {pack_name}. Error: {str(e)}")
        else:
            print(f"Invalid pack folder or manifest not found for pack: {pack_name}")

    return pack_list


def get_behavior_pack_info():
    pack_list = []
    behavior_packs_path = f'C:\\Users\\{username}\\AppData\\Local\\Packages\\Microsoft.MinecraftUWP_8wekyb3d8bbwe\\LocalState\\games\\com.mojang\\behavior_packs'
    
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
                        'version': manifest_data.get('header', {}).get('version', ''),
                        'path': pack_folder_path
                    }
                    pack_list.append(pack_info)
                except json.JSONDecodeError as e:
                    print(f"Error loading JSON in pack: {pack_name}. Error: {str(e)}")
        else:
            print(f"Invalid pack folder or manifest not found for pack: {pack_name}")

    return pack_list

def delete_resource_pack(uuid):
    resource_packs_path = f"C:\\Users\\{username}\\AppData\\Local\\Packages\\Microsoft.MinecraftUWP_8wekyb3d8bbwe\\LocalState\\games\\com.mojang\\resource_packs"

    packs_info = get_resource_pack_info()
    for i in packs_info:
        if i['uuid'] == uuid:
            shutil.rmtree(i['path'])
    print('completed')


def delete_behavior_pack(uuid):
    behavior_packs_path = f"C:\\Users\\{username}\\AppData\\Local\\Packages\\Microsoft.MinecraftUWP_8wekyb3d8bbwe\\LocalState\\games\\com.mojang\\behavior_packs"

    packs_info = get_behavior_pack_info()
    for i in packs_info:
        if i['uuid'] == uuid:
            shutil.rmtree(i['path'])
    print('completed')


def export_world(folder, path):
    if os.path.isdir(f'C:\\Bedrock\\temp'):
        shutil.rmtree(f'C:\\Bedrock\\temp')

    if os.path.exists('C:\Bedrock\world.zip'):
        os.remove ('C:\Bedrock\world.zip')
    if os.path.exists('C:\Bedrock\world.mcworld'):
        os.remove ('C:\Bedrock\world.mcworld')

    shutil.copytree(os.path.join(f'C:\\Users\\{username}\\AppData\\Local\\Packages\\Microsoft.MinecraftUWP_8wekyb3d8bbwe\\LocalState\\games\\com.mojang\\minecraftWorlds', folder), f'C:\\Bedrock\\temp')

    os.system (f'powershell -c Compress-Archive -Path "C:\\Bedrock\\temp" -DestinationPath "C:\Bedrock\world.zip"')

    os.rename('C:\Bedrock\world.zip', 'C:\Bedrock\world.mcworld')

    try:
        shutil.move ('C:\Bedrock\world.mcworld', path)
        return ('completed')
    except:
        print (f'file exists: {path}\world.mcworld')
        return (f'file exists: {path}\world.mcworld')
        
def dissable_resource_packs(folder):
    try:
        #os.remove(f'C:\\Users\\{username}\\AppData\\Local\\Packages\\Microsoft.MinecraftUWP_8wekyb3d8bbwe\\LocalState\\games\\com.mojang\\minecraftWorlds\\' + folder + '\\world_behavior_packs.json')
        os.remove(f'C:\\Users\\{username}\\AppData\\Local\\Packages\\Microsoft.MinecraftUWP_8wekyb3d8bbwe\\LocalState\\games\\com.mojang\\minecraftWorlds\\' + folder + '\\world_resource_packs.json')
        print('removed world_resource_packs.json file')
    except:
        print('no world_resource_packs file')


    try:
        shutil.rmtree(f'C:\\Users\\{username}\\AppData\\Local\\Packages\\Microsoft.MinecraftUWP_8wekyb3d8bbwe\\LocalState\\games\\com.mojang\\minecraftWorlds\\' + folder + '\\resource_packs')
        print('removed resource_packs')
    except:
        print('no resource_packs file')


def dissable_behavior_packs(folder):
    try:
        os.remove(f'C:\\Users\\{username}\\AppData\\Local\\Packages\\Microsoft.MinecraftUWP_8wekyb3d8bbwe\\LocalState\\games\\com.mojang\\minecraftWorlds\\' + folder + '\\world_behavior_packs.json')
        #os.remove(f'C:\\Users\\{username}\\AppData\\Local\\Packages\\Microsoft.MinecraftUWP_8wekyb3d8bbwe\\LocalState\\games\\com.mojang\\minecraftWorlds\\' + folder + '\\world_resource_packs.json')
        print('removed world_behavior_packs.json')
    except:
        print('no world_behavior_packs.json file')

    try:
        shutil.rmtree(f'C:\\Users\\{username}\\AppData\\Local\\Packages\\Microsoft.MinecraftUWP_8wekyb3d8bbwe\\LocalState\\games\\com.mojang\\minecraftWorlds\\' + folder + '\\behavior_packs')
        #os.remove(f'C:\\Users\\{username}\\AppData\\Local\\Packages\\Microsoft.MinecraftUWP_8wekyb3d8bbwe\\LocalState\\games\\com.mojang\\minecraftWorlds\\' + folder + '\\world_resource_packs.json')
        print('removed behavior_packs')
    except:
        print('no behavior_packs file')



def apply_resource_pack(world, uuid, version=[0, 0, 1]):
    try:
        f = open (f'C:\\Users\\{username}\\AppData\\Local\\Packages\\Microsoft.MinecraftUWP_8wekyb3d8bbwe\\LocalState\\games\\com.mojang\\minecraftWorlds\\' + world + '\\world_resource_packs.json', 'r')
        current_packs = json.loads(f.read())
        f.close()
    except:
        current_packs = []

    f = open (f'C:\\Users\\{username}\\AppData\\Local\\Packages\\Microsoft.MinecraftUWP_8wekyb3d8bbwe\\LocalState\\games\\com.mojang\\minecraftWorlds\\' + world + '\\world_resource_packs.json', 'w')
    pack = {
        'pack_id' : uuid,
        'version' : version
    }
    current_packs.append(pack)
    #print(current_packs)
    f.write (json.dumps(current_packs))

    #apply_resource_pack('test', '461deaee-c9a1-41a0-aca3-4585fd4eb839')


def apply_behavior_pack(world, uuid, version=[0, 0, 1]):
    try:
        f = open (f'C:\\Users\\{username}\\AppData\\Local\\Packages\\Microsoft.MinecraftUWP_8wekyb3d8bbwe\\LocalState\\games\\com.mojang\\minecraftWorlds\\' + world + '\\world_behavior_packs.json', 'r')
        current_packs = json.loads(f.read())
        f.close()
    except:
        current_packs = []

    f = open (f'C:\\Users\\{username}\\AppData\\Local\\Packages\\Microsoft.MinecraftUWP_8wekyb3d8bbwe\\LocalState\\games\\com.mojang\\minecraftWorlds\\' + world + '\\world_behavior_packs.json', 'w')
    pack = {
        'pack_id' : uuid,
        'version' : version
    }
    current_packs.append(pack)
    #print(current_packs)
    f.write (json.dumps(current_packs))

    #apply_resource_pack('test', '461deaee-c9a1-41a0-aca3-4585fd4eb839')




