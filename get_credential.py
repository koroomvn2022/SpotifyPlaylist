import requests
from requests.exceptions import *
import base64
import yaml
from pathlib import Path

def getAuthorizationCode():

    with open(r'D:\sdk_python\Glue\workspace\spotify\variables.yaml') as file:
        info = yaml.safe_load(file)

    
    CLIENT_ID = info.get('CLIENT_ID', '')
    CLIENT_SECRET = info.get('CLIENT_SECRET', '')

    if not CLIENT_ID or not CLIENT_SECRET:
        print('there is no CLIENT_ID or CLIENT_SECRET')
    else:
        urlAuth = 'https://accounts.spotify.com/authorize'

        paramsAuth = {
            'client_id': CLIENT_ID
            , 'response_type': 'code'
            , 'redirect_uri': 'https://localhost'
            , 'scope': 'ugc-image-upload user-read-playback-state user-modify-playback-state user-read-currently-playing app-remote-control streaming playlist-read-private playlist-read-collaborative playlist-modify-private playlist-modify-public user-follow-modify user-follow-read user-read-playback-position user-top-read user-read-recently-played user-library-modify user-library-read user-read-email user-read-private'  
        }

        try:

            responseAuth = requests.get(url=urlAuth, params=paramsAuth)

        except MissingSchema as e:
            
            print(f'Error: {e}')
            raise

        except HTTPError as e:

            print(f'Error: {e}')
            raise

        except ConnectionError as e:

            print(f'Request error: {e}')
            raise
        except Exception as e:

            print(f'Error: {e}')
            raise

        print('Get Authorization Code successfully')
        return print(responseAuth.url)


def getAccessToken(code):

    with open(r'D:\sdk_python\Glue\workspace\spotify\variables.yaml') as file:
        info = yaml.safe_load(file)


    CLIENT_ID = info.get('CLIENT_ID', '')
    CLIENT_SECRET = info.get('CLIENT_SECRET', '')

    if not CLIENT_ID or not CLIENT_SECRET:
        print('there is no CLIENT_ID or CLIENT_SECRET')
    else:
        credentials = f'{CLIENT_ID}:{CLIENT_SECRET}'
        credentialsBase64 = base64.b64encode(credentials.encode()).decode()

        urlToken = 'https://accounts.spotify.com/api/token'

        headersToken = {
            'Authorization': f'Basic {credentialsBase64}'
            , 'Content-Type': 'application/x-www-form-urlencoded'
        }
        dataToken = {
            'grant_type': 'authorization_code'
            , 'code': code
            , 'redirect_uri': 'https://localhost'
        }
        try:
            responseToken = requests.post(url=urlToken, data=dataToken, headers=headersToken)
        
        except MissingSchema as e:
            
            print(f'Error: {e}')
            raise

        except HTTPError as e:

            print(f'Error: {e}')
            raise

        except ConnectionError as e:

            print(f'Request error: {e}')
            raise
        except Exception as e:

            print(f'Error: {e}')
            raise
        
        try:
            accessToken = responseToken.json()['access_token']

            with open(r'D:\sdk_python\Glue\workspace\spotify\variables.yaml', 'w', newline='\n') as file:

                info['ACCESS_TOKEN'] = accessToken
                yaml.dump(info, file)

            print('Get access token successfully')
        except Exception as e:
            print(f'Error: {e}')

if __name__ == '__main__':
    # getAuthorizationCode()
    code = 'AQDP8Uej4hf6pm8914UCGo0rmsO8Z2hyxSDRNzAOZkh7g6DalMTqD2B_0069SEBZrhda1PpLu2OUIquWbeUlTvUZSU6vnjVcr3LvPAd8vpmEbfRvpmIyU5geISGakCb3wz7DT72_JTnk7eOh1lZsbXgezVEMoPtsnvbHbA4qJ7mgG8rdjE3cJf7rUzJV-S7rAFYP00sLq2TyTsgEVBheGfQYgunvOCaX0DNUFfy0TZPF99CrffhsymsPj2mxXzlwGyDdl3GCdMpvIr9hNJ25cBsNy_zQ4sXL0jBjRcIaz4KnLoXIVy9cW5C7DkmhkwvTZ1cuEe4Oe37kGmHiizbmz6wxveBhdGeC27mqNmanZDs55EL5EceHCaEpip8Ue5HsyqlJdG8He18kLHGG99L3EPlIR5-ESFZU3rKmJ2Y4oL_wcUu6wsjKBe1xYLhUbMjjBfXld5EGK_yUU594vsZomfNyRLfD9XNJO-iyzwZAbqDf-cBRzU0d1I9E3c3GJ90dO_kp6m5pgolzMwnV6YmNnANkszWjx_c5y8k_yey0cHI2ZP-JVtlatjrQXSJLAcpAlB2yDgK-1mKWIY2ity-n73E5j8Tpu7eDk8OLrLUP8u4rk5Qs5HmJkzNPhQQN3fBasMAWW0lSqrQcWBWDdR3SZ12dG6oNoapE8H2D9orLU0eIvunIJA9v4L4LJQ8d71Nl6nlfU-VXUw'
    getAccessToken(code)