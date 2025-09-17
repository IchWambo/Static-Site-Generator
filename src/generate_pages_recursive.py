import os
from generate_page import generate_page
def generate_pages_recursive(dir_path_content, template_path, dest_dir_path, basepath="/"):
    list_dirs = os.listdir(dir_path_content)
    for dir in list_dirs:
        new_path = os.path.join(dir_path_content, dir)
        new_dest = os.path.join(dest_dir_path, dir)
        if os.path.isdir(new_path):
            generate_pages_recursive(new_path, template_path, new_dest, basepath)
        elif os.path.isfile(new_path):
            split_dest, _ = os.path.splitext(new_dest)
            final_dest = split_dest + ".html"
            generate_page(new_path, template_path, final_dest, basepath)
            
            
            
            



