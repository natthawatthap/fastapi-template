import os
import shutil

def remove_pycache_dirs(root_dir='.'):
    for root, dirs, files in os.walk(root_dir):
        for dir_name in dirs:
            if dir_name == '__pycache__':
                dir_path = os.path.join(root, dir_name)
                print(f'Removing {dir_path}')
                shutil.rmtree(dir_path)

if __name__ == '__main__':
    remove_pycache_dirs()
