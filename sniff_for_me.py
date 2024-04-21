from db import Db
from api import ExecApi
import requests

# mydb = Db()
# exec_api = ExecApi()
# images = mydb.get_images()


def download_gifs():
    mydb = Db()
    images = mydb.get_images()
    for index, image in enumerate(images):
        print(f'i: {index}, img: {image}')
        # print(image[31:])
        with open(f'tmp/{image[31:]}.gif', 'wb') as f:
            f.write(requests.get(image).content)
        f.close()


def add_extension_to_files():
    import os
    path = os.getcwd()
    print(f'{path}/tmp/')
    for index, file in enumerate([f for f in os.listdir(f'{path}/tmp/')]):
        print(f'i: {index}, file: {file}')
        os.rename(f'{path}/tmp/{file}', f'{path}/tmp/{file}.gif')
    print('changed!')


# add_extension_to_files()
