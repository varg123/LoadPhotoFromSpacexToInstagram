import requests


def fetch_huble_collection(name_collection='spacecraft'):
    url_photos_collection = f'http://hubblesite.org/api/v3/images/{name_collection}?page=all'
    photos_colletcion_data = requests.get(url_photos_collection).json()
    ids_photos = [photo_info['id'] for photo_info in photos_colletcion_data]
    for id_photo in ids_photos:
        url_photo_info = f'http://hubblesite.org/api/v3/image/{id_photo}'
        url_photo_data = requests.get(url_photo_info).json()
        url_photo = url_photo_data['image_files'][-1]['file_url']
        yield url_photo
