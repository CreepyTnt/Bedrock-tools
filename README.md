### This project is just the api for Bedrock Launcher (can be found on my profile). Because i am lazy and frequently forget I even have this repo open, this will be out of date sometimes. You can find the latest "bedrock_tools.py" file under my Bedrock Launcher repo.

# Bedrock-tools
A suite of tools for Minecraft Bedrock such as backups, add-on management, and more! This project is in development so please leave feedback about bugs.

## **Bedrock Tools currently only supports Windows 10/11, however, support for android may be added in the future

# Installation

Simply download the code and import it into your project:
``` python
import bedrock_tools as mc
```

# Usage

### It is recommended that you take a manual backup of your minecraft worlds before using this because this project is still in development and could potentially delete r currupt your games saves if there is a glitch.


### Backup com.mojang
You can backup the entire com.mojang folder (C:\Users\<username>\AppData\Local\Packages\Microsoft.MinecraftUWP_8wekyb3d8bbwe\LocalState\games\com.mojang) like this:
``` python
path = D:\minecraft_backup
mc.backup_worlds(path) #overwrites everything in the provided path. Use with caution
```


### Backup minecraftWorlds
You can backup only your worlds (C:\Users\<username>\AppData\Local\Packages\Microsoft.MinecraftUWP_8wekyb3d8bbwe\LocalState\games\com.mojang\minecraftWorlds) like this:
``` python
path = D:\minecraft_backup
mc.backup_worlds(path) #Overwrites only the minecraftworlds directory in the provided location. It shoudn't effect anything else, however, proceed with caution.
```

### Get world dict.

Get a dictionary of all of your Minecraft worlds and their corrisponding folder like this:
``` python
mc.get_world_dict()
print (mc.world_dict)
```

### backup minecraft settings
You can backup minecraft settings (FOV, keyboard settings, ect.) like this.
``` python
path = D:\minecraft_backup
mc.backup_settings(path) #creates a new folder (options) inside of the provided location containing the options.txt file. this should not overwrite exsisting backups.
```

### Get world info
The first step to get info for a particular world is to look up the folder that the world is located in using get_world_dict.
``` python
mc.get_world_dict()
```
After looking up the world's foder name, you can get info for it like this:
``` python
mc.get_world_info(folder_name)
```
### clear pack history
After you get the world dict, you can clear resource and behavior pack history. This is especially usefull when deleting packs because in the game, packs may continue to show up after you delete them because the game retains a log of all applied packs. You can clear the pack history like this:
``` python
mc.clear_pack_history(folder_name) #this deletes things in your com.mojang folder so precede with caution.
```


### start Minecraft
To start minecraft with or without [fov-changer](https://github.com/xroix/MCBE-Win10-FOV-Changer), run this function:
``` python
mc.start_game(False) #true starts minecraft and fov changer (if it's located in C:\Bedrock), false only sarts minecraft
```

### import an add-on or world as .mcpack or .mcworld
you can import a world or pack like this:
``` python
path = 'C:\path\to\world\or\pack'
mc.import_pack(path)
```

### get resource pack info
you can get info (name, uuid, discription, and version) of every resource pack like this:
``` python
mc.get_resource_pack_info() #returns a list of dictionaries containing info.
```
For some reason, the manifest files of some packs are not valid json and cannot be read. These will be skipped when getting pack info.


### get behavior pack info
you can get info about behavior packs (name, description, uuid, and version) like this:
``` python
mc.get_behavior_pack_info() #returns a list of dictionaries containing info.
```
For some reason, the manifest files of some packs are not valid json and cannot be read. These will be skipped when getting pack info.


### delete a resource pack
To delete a resource pack, you will need to obtain the uuid of the pack using mc.get_resource_pack_info()
``` python
uuid = mc.get_resource_pack_info()['uuid']
mc.delete_resource_pack (uuid)
```
Procede with caution!


### delete a behavior pack
To delete a behavior pack, you will need to obtain the uuid of the pack using mc.get_behavior_pack_info()
``` python
uuid = mc.get_behavior_pack_info()['uuid']
mc.delete_behavior_pack (uuid)
```
Procede with caution!


### export world
After getting the folder name of your world using get_world_dict,
``` python
mc.get_world_dict
```
you can export the world like this:
``` python
mc.export_world (folder_name, export_path)
```


### disable resource packs
you can disable all resource packs in a world like this:
``` python
mc.disable_resource_packs (world_folder) #you need to get the world folder name with mc.get_world_dict as previously explained.
```

### disable behavior packs
you can disable all behavior packs in a world like this:
``` python
mc.disable_behavior_packs (world_folder) #you need to get the world folder name with mc.get_world_dict as previously explained.
```


### apply resource packs
After you get the world folder and pack uuid as previously explained, you can apply resource packs like this:
``` python 
mc.apply_resource_packs(world_folder, uuid)
```

### apply resource packs
After you get the world folder and pack uuid as previously explained, you can apply behavior packs like this:
``` python 
mc.apply_behavior_packs(world_folder, uuid)
```





### More features coming soon!

*If you get errors with the paths, try changing "\\" to "\/" or "\\\\". https://stackoverflow.com/questions/2953834/how-should-i-write-a-windows-path-in-a-python-string-literal*
