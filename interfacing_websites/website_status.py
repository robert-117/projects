import requests
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('url', action='extend', nargs='+', help='check status codes for websites')

args = parser.parse_args()
url = args.url

def fetch_status(url):
    for website in url:
        try:
            response = requests.get(website)
        except requests.HTTPError as e:
            print(e)
        finally:
            print(f'status code {response.status_code}: {website}')

fetch_status(url)