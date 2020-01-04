import os
import cat_service
import subprocess

def main():
    print_header()
    folder1=get_or_create_output_folder()
    print("Created or found folder at :{}".format(folder1))
    download_cats(folder1)
    display_cats(folder1)

def print_header():
    print('----------------------------------------------')
    print('                   CAT FACTORY')
    print('----------------------------------------------')


def get_or_create_output_folder():
    folder='cat pictures 2'
    base_folder=os.path.dirname(__file__)
    filepath=os.path.join(base_folder,folder)#building out the file path

    #creating the directory
    if not os.pat=h.exists(filepath) or not os.path.isdir(filepath):
        print('Creating new directory at {}'.format(filepath))
        os.mkdir(filepath)
    return (filepath)

def download_cats(folder):
    cat_count=8
    for i in range(1, cat_count+1):
        cat_name='LOLcat_{}'.format(i)
        print (cat_name)
        cat_service.download_cats(folder,cat_name)

def display_cats(folder):
    subprocess.call(['open', folder])



if __name__=='__main__':
    main()