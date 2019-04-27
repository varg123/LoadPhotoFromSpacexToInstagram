import requests


def fetch_spacex_last_launch():
    url = 'https://api.spacexdata.com/v3/launches/latest'
    response_spacex = requests.get(url)
    if not response_spacex.ok:
            response_spacex.raise_for_status()
    return response_spacex.json()['links']['flickr_images']
