import os
import shutil

def delete_files(files_to_delete, dir="public/"):
    if len(files_to_delete) == 0:
        return
    if len(files_to_delete) > 1:
        delete_files(files_to_delete[1:], dir)

    if os.path.isfile(f"{dir}{files_to_delete[0]}"):
        os.remove(f"{dir}{files_to_delete[0]}")
    elif os.path.isdir(f"{dir}{files_to_delete[0]}"):
        new_dir = os.path.join(f"{dir}{files_to_delete[0]}/")
        new_files = os.listdir(new_dir)
        delete_files(new_files, new_dir)
        os.rmdir(f"{dir}{files_to_delete[0]}")

def copy_files(files_to_copy, src_dir="static/",dst_dir="public/"):
    if len(files_to_copy) == 0:
        return
    if os.path.isfile(f"{src_dir}{files_to_copy[0]}"):
        shutil.copy(f"{src_dir}{files_to_copy[0]}",dst_dir)
    elif os.path.isdir(f"{src_dir}{files_to_copy[0]}"):
        os.mkdir(f"{dst_dir}{files_to_copy[0]}")
        new_src_dir = os.path.join(f"{src_dir}{files_to_copy[0]}/")
        new_dst_dir = os.path.join(f"{dst_dir}{files_to_copy[0]}/")
        new_files_to_copy = os.listdir(new_src_dir)
        copy_files(new_files_to_copy, new_src_dir, new_dst_dir)
    if len(files_to_copy) > 1:
        copy_files(files_to_copy[1:],src_dir, dst_dir)
    
if os.path.exists("public") == True:
    files_to_delete = os.listdir("public")
    delete_files(files_to_delete)
else:
    os.mkdir("public")

files_to_copy = os.listdir("static")
copy_files(files_to_copy)

