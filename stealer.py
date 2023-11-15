import requests
import json
import stealer_type as steal
from bs4 import BeautifulSoup as bsoup
from string import Template

GP_URL_TEMPLATE = Template("https://www.songsterr.com/api/meta/$id/revisions")
SONGSTERR_SEARCH_TEMPLATE = Template("https://www.songsterr.com/?pattern=$search_string")


def get_gp_file(request_string: str, stealer_type: str):
    if stealer_type is steal.BY_URL:
        song_id = get_song_id(request_string)
    elif stealer_type is steal.BY_SEARCH_STRING:
        song_id = get_song_id_from_search_string(request_string)
    else:
        raise Exception("wrong.stealer.type")

    return get_gp_file_url(song_id)


def get_by_string(search_string: str):
    song_id = get_song_id_from_search_string(search_string)
    return get_gp_file_url(song_id)


def get_song_id_from_search_string(search_string: str):
    url = SONGSTERR_SEARCH_TEMPLATE.substitute(search_string=search_string)
    r = requests.get(url)
    soup = bsoup(r.text, 'html.parser')
    meta = soup.find_all('script', attrs={'id': 'state'})
    jsonified = json.loads(str(meta[0].string))
    return jsonified['songs']['songs']['list'][0]['songId']


def get_song_id(url: str):
    r = requests.get(url)
    soup = bsoup(r.text, 'html.parser')
    meta = soup.find_all('script', attrs={'id': 'state'})
    meta_string = meta[0].string
    jsonified = json.loads(str(meta[0].string))
    return jsonified['meta']['songId']


def get_gp_file_url(song_id: int):
    url = GP_URL_TEMPLATE.substitute(id=song_id)
    r = requests.get(url)
    jsonified = json.loads(r.text)
    return jsonified[0]['source']
