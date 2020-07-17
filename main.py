import os
import shutil

import getpass
import win32api,win32con
import webbrowser
# 获取当前用户名
user_name = getpass.getuser()
#获取当前目录
sourcefile_source=os.path.dirname(os.path.abspath(','))

destinationfile_init="C:\\Users\\"+user_name+"\\AppData\\Roaming\\Adobe\\CameraRaw\\Settings"

source_path = os.path.abspath(sourcefile_source)
target_path = os.path.abspath(destinationfile_init)

 