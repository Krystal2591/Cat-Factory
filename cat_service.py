import requests
import shutil
import os

def download_cats(folder, name):
    url1='http://consuming-python-services-api.azurewebsites.net/cats/random'
    cat=get_data_from_url(url1)
    save_cat_image(folder, name, cat)


def get_data_from_url(url):
    response= requests.get(url, stream= True)
    return response.raw

def save_cat_image(folder, name, cat):
    filepath=os.path.join(folder, name+ '.jpg')
    with open(filepath, 'wb') as fout:
        shutil.copyfileobj(cat, fout)



