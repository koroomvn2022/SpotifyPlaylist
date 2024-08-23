import requests
from requests.exceptions import *
from bs4 import BeautifulSoup
import datetime
import yaml
import html5lib
import json
import pandas as pd
from fake_useragent import UserAgent
from get_tracks import *
from get_credential import *

def create_playlist():
    # Get infomation

    with open(r'D:\sdk_python\Glue\workspace\spotify\variables.yaml') as file:
        info = yaml.safe_load(file)

    # Set headers
    ACCESS_TOKEN = info.get('ACCESS_TOKEN', '')

    headers = {
        'Authorization': 'Bearer ' + ACCESS_TOKEN
    }


    # Get date
    date = datetime.date.today()
    dateSTR = date.strftime('%Y-%m-%d')

    # Put Items into playlist
    if not ACCESS_TOKEN:

        print('There is no ACCESS_TOKEN')

    else:
        #TODO: Get tracls

        content = getResponse(dateSTR)
        tracks = getTracks(content)

        
        #TODO Get user id

        urlUserProfile = 'https://api.spotify.com/v1/me'

        print('The process of getting user_id is underway')
        try:

            userId = requests.get(urlUserProfile, headers=headers).json()['id']

        except Exception as e:
            print(f'Error: {e}')

        print(f'Successfully got userId')

        #TODO: create playlists

        urlPlayLists = f'https://api.spotify.com/v1/users/{userId}/playlists'

        bodyPlayLists = {
            'name': f'TOP_100_{dateSTR}'
        }
        print('The process of creating a playlist is underway')
        try:

            responsePlayList = requests.post(url=urlPlayLists, data=json.dumps(bodyPlayLists), headers=headers)
        
        except Exception as e:
            print(f'Error: {e}')
            raise e

        responsePlayList.content

        playListId = responsePlayList.json()['id']

        #TODO: Get track id
        print('The process of getting track id is underway')
        try:
            trackIds = []
            for track in tracks:
                responseTrack = requests.get(
                    url='https://api.spotify.com/v1/search'
                    , params={
                        'q': f'track:{track}'
                        , 'type': 'track'
                        , 'limit': 1
                    }
                    , headers=headers
                )
                trackId = responseTrack.json()['tracks']['items'][0]['id']
                trackIds.append(trackId)

        except Exception as e:
            print(f'Error: {e}')
            raise e

        #TODO: Add track to playlist
        print('The process of adding tracks to the playlist is underway.')
        try:
            trackURIS = [ f'spotify:track:{trackId}' for trackId in trackIds]
            responseAddTrack = requests.post(
                url=f'https://api.spotify.com/v1/playlists/{playListId}/tracks'
                , data=json.dumps({
                    'uris': trackURIS
                })
                , headers=headers
            )
        except Exception as e:
            print(f'Error: {e}')
            raise e

if __name__ == '__main__':
    create_playlist()