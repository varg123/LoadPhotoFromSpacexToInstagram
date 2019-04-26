import requests


def fetch_spacex_last_launch():
    url = 'https://api.spacexdata.com/v3/launches/latest'
    return requests.get(url).json()['links']['flickr_images']
