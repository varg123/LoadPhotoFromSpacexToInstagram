import requests
from os import mkdir, listdir
from os.path import exists, isfile, join, splitext
from fetch_spacex import fetch_spacex_last_launch
from fetch_huble import fetch_huble_collection
from insta_publish import publish_on_instagram

IMAGES_PATH = 'images'


def download_image(name, url):
    if not exists(IMAGES_PATH):
        mkdir(IMAGES_PATH)
    _, file_extension = splitext(url)
    with open(join(IMAGES_PATH, f'{name}.{file_extension}'), 'wb') as file:
        response_image = requests.get(url)
        if not response_image.ok:
                response_image.raise_for_status()
        file.write(response_image.content)


def fetch_save_images():
    if exists(IMAGES_PATH):
        return [
            join(IMAGES_PATH, name)
            for name in listdir(IMAGES_PATH)
            if isfile(join(IMAGES_PATH, name))
        ]


def main():
    urls_spacex_images = fetch_spacex_last_launch()
    count_spacex_images = len(urls_spacex_images)
    for index, img_url in enumerate(urls_spacex_images, start=1):
        print(f'Скачивается фото с Spacex - {index}/{count_spacex_images}')
        download_image(f'spacex{index}', img_url)
    urls_huble_images = list(fetch_huble_collection())
    count_huble_images = len(urls_huble_images)
    for index, img_url in enumerate(urls_huble_images, start=1):
        print(f'Скачивается фото с Huble - {index}/{count_huble_images}')
        download_image(f'huble{index}', img_url)
    print('Публикуем сохранённые фотографии в Инстаграм')
    publish_on_instagram(fetch_save_images())

if __name__ == '__main__':
    main()
