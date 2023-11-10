import requests
import json
from bs4 import BeautifulSoup as bsoup
from string import Template

GP_URL_TEMPLATE = Template("https://www.songsterr.com/api/meta/$id/revisions")


def get_gp_file(url: str):
    song_id = get_song_id(url)
    return get_gp_file_url(song_id)


def get_song_id(url: str):
    r = requests.get(url)
    soup = bsoup(r.text, 'html.parser')
    meta = soup.find_all('script', attrs={'id': 'state'})
    meta_string = meta[0].string
    jsonified = json.loads(str(meta[0].string))
    return jsonified['meta']['songId']


def get_gp_file_url(song_id : int):
    url = GP_URL_TEMPLATE.substitute(id=song_id)
    r = requests.get(url)
    jsonified = json.loads(r.text)
    return jsonified[0]['source']
