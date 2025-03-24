import requests
import json

URL = f"https://rickandmortyapi.com/"

def get_character_inf(url):
    ch_url=(f'{url}/api/character')
    response = requests.get(ch_url)
    inf = json.loads(response.text)
    print(inf)
    len(inf)
    return inf

def out(info):
    for i in range(20):
        print(f'Name of creature: '
              +f'{info['results'][i]['name']}. '
              +f'Species: '
              +f'{info['results'][i]['species']}. '
              +f'Is it alive?: '
              +f'{info['results'][i]['status']}. '
              +f'Gender: '
              +f'{info['results'][i]['gender']}. '
              +f'location: '
              +f'{info['results'][i]['location']['name']}. ')

out(get_character_inf(URL))
