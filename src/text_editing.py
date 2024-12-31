import os
import shutil
import re
from blocks import markdown_to_html_node


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
        
        
def extract_title(markdown):
    if re.match(r"(?<!#)\#\ .+", markdown):
        match = (re.findall(r"(?<!#)\#\ .+",markdown))[0]
        return match.strip(" #")
    else:
        raise Exception("No header (h1) in markdown file")
    
def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    with open(from_path) as markdown:
        markdown_text = markdown.read()
    with open(template_path) as template:
        template_text = template.read()
    h1_title = extract_title(markdown_text)
    html_content = markdown_to_html_node(markdown_text).to_html()
    website = template_text.replace("{{ Title }}",h1_title).replace("{{ Content }}",html_content)
    try:
        with open(dest_path,"x") as index:
            index.write(website)
    except FileNotFoundError:
        paths = dest_path.split("/")
        paths.pop(-1)
        path_tobecreated = "/".join(paths)
        os.makedirs(path_tobecreated)

        with open(dest_path,"x") as index:
            index.write(website)

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    if dir_path_content.endswith("/"):
        raise Exception("make sure there is no '/' at the end of your folder locations")
    content = os.listdir(dir_path_content)
    if len(content) == 0:
        return
    for file in content:
        path = f"{dir_path_content}/{file}"
        new_dest_dir_path = os.path.join(dest_dir_path, path.strip("content/"))
        if os.path.isdir(path):
            os.mkdir(new_dest_dir_path)
            generate_pages_recursive(path, template_path, dest_dir_path)
        elif os.path.isfile(path):
            html_file_path_and_name = new_dest_dir_path.replace(".md",".html")
            generate_page(path, template_path, html_file_path_and_name)



        

