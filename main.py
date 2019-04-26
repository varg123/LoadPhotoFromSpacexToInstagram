import requests
from os import mkdir, listdir
from os.path import exists, isfile
from fetch_spacex import fetch_spacex_last_launch
from fetch_huble import fetch_huble_collection
from insta_publish import publish_on_instagram


def donwload_image(name, url):
    if not exists('images'):
        mkdir('images')
    file_extension = get_file_extension(url)
    with open(f'images/{name}.{file_extension}', 'wb') as file:
        file.write(requests.get(url).content)


def get_file_extension(url):
    return url.split('.')[-1]


def fetch_save_images():
    if exists('images'):
        return [
            f'images/{name}'
            for name in listdir('images')
            if isfile(f'images/{name}')
        ]


def main():
    urls_spacex_images = fetch_spacex_last_launch()
    count_spacex_images = len(urls_spacex_images)
    for index, img_url in enumerate(urls_spacex_images, start=1):
        print(f'Скачивается фото с Spacex - {index}/{count_spacex_images}')
        donwload_image(f'spacex{index}', img_url)
    urls_huble_images = list(fetch_huble_collection())
    count_huble_images = len(urls_huble_images)
    for index, img_url in enumerate(urls_huble_images, start=1):
        print(f'Скачивается фото с Huble - {index}/{count_huble_images}')
        donwload_image(f'huble{index}', img_url)
    print('Публикуем сохранённые фотографии в Инстаграм')
    publish_on_instagram(fetch_save_images())

if __name__ == '__main__':
    main()
