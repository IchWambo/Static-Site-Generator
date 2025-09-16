import os, shutil, sys

def copy_contents(source, destination):
    #path_s = "/home/wambo/bootdev/Static_Site_Generator/Static-Site-Generator/src/static"
    #path_d = "/home/wambo/bootdev/Static_Site_Generator/Static-Site-Generator/src/public"
    if not os.path.isdir(source):
        raise Exception("invalid source")
    if os.path.isdir(destination):
        shutil.rmtree(destination)
    os.mkdir(destination)
    directories_src = os.listdir(source)
    for directory in directories_src:
        new_source = os.path.join(source, directory)
        new_dest = os.path.join(destination, directory)
        if os.path.isdir(new_source):
            print("creating dir:", new_dest)
            os.mkdir(new_dest)
            copy_contents(new_source, new_dest)
        else:
            print("copying file:", new_source, "->", new_dest)
            shutil.copy(new_source, new_dest)    

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("usage: python src/copystatic.py <source> <destination>")
        sys.exit(1)
    src, dst = sys.argv[1], sys.argv[2]
    copy_contents(src, dst)