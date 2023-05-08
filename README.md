# Bedrock-tools
A suite of tools for Minecraft Bedrock such as automatic backups, add-on management, and more!

## **Bedrock Tools currently only supports Windows 10/11, however, support for android may be added in the future

# Installation

Simply download the code and import it into your project:
``` python
import bedrock_tools as mc
```

# Usage

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
### start Minecraft
To start minecraft with or without [fov-changer](https://github.com/xroix/MCBE-Win10-FOV-Changer), run this function:
``` python
mc.start_game(False) #true starts minecraft and fov changer (if it's located in C:\Bedrock), false only sarts minecraft
```



### More features such as add-on management coming soon!

*If you get errors with the paths, try changing "\\" to "\/" or "\\\\". https://stackoverflow.com/questions/2953834/how-should-i-write-a-windows-path-in-a-python-string-literal*
