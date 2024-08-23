import requests
from requests.exceptions import *
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

def getResponse(dateSTR):

    #TODO: Get date

    ua = UserAgent()
    url = f'https://www.billboard.com/charts/hot-100/{dateSTR}/'

    try:
        #TODO: Get Response
        response = requests.get(
            url=url
            , headers = {'User-Agent': ua.random}
        )
        
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

    print('Get response successfully')
    return response.content

def getTracks(content):
    #TODO: Make soup
    soup = BeautifulSoup(content, 'html5lib')


    #TODO: Get track
    try:
        chartResultsList = soup.find(
            'div'
            , class_='chart-results-list'
        )
        chartResultListRows = chartResultsList.find_all(
            'div'
            , class_='o-chart-results-list-row-container'
        )

        titleOfAStories = [ item.find('h3', id='title-of-a-story') for item in chartResultListRows]

        tracks = [item.string.strip() for item in titleOfAStories]

    except Exception as e:
        print(f'Error: {e}')
        raise

    print('Get tracks successfully')
    print(tracks)
    return tracks

if __name__ == '__main__':
    print(getTracks(getResponse('2024-08-18')))