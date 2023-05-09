import os
import shutil
import datetime

folder_to_read = os.path.join(os.path.expanduser("~"),"Downloads")

folder_to_store = os.path.join(os.path.expanduser("~"),"Downloads/palace")

today = datetime.date.today()
today_string = today.strftime('%Y-%m-%d')

files_on_folder = os.listdir(folder_to_read)

for file in files_on_folder:
    extention = os.path.splitext(file)[1]

    if extention:

        path_file = os.path.join(folder_to_read, file)

        if os.path.isfile(path_file):

            destiny = os.path.join(folder_to_store,extention[1:],today_string)

            if not os.path.exists(destiny):
                os.makedirs(destiny)

            shutil.move(path_file, destiny)
