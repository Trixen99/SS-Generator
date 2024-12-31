##### **** HAS TO BE RUN FROM ROOT FOLDER, USE ./MAIN.SH TO START **** #####
import os
from text_editing import *


    
if os.path.exists("public") == True:
    files_to_delete = os.listdir("public")
    delete_files(files_to_delete)
else:
    os.mkdir("public")

files_to_copy = os.listdir("static")
copy_files(files_to_copy)

generate_pages_recursive("content", "template.html", "public")









                



