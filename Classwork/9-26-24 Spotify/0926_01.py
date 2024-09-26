#this is taken from the spotify documentation
#base 64 allows us to encode our string
import requests
from base64 import b64encode

client_id = "1ddc5f4af9d34bdf9915ff09951364de"
client_secret = "6a01503b87c84ab185a1fa94f65eb7c3"

auth_url = 'https://accounts.spotify.com/api/token'
auth_header = 'Basic ' + b64encode((client_id + ':' + client_secret).encode()).decode()

auth_data = {
    'grant_type': 'client_credentials'
}

#we are POSTING something to the server in order to RETURN the token
auth_response = requests.post(auth_url, headers={'Authorization': auth_header}, data=auth_data)

if auth_response.status_code == 200:
    token = auth_response.json().get('access_token')
    print('Token:', token)
else:
    print('Error:', auth_response.status_code)
    print(auth_response.text)

#Now we can try requesting information
artist_id = "4Z8W4fKeB5YxbusRsdQVPb"
url = f"https://api.spotify.com/v1/artists/{artist_id}"

headers = {
    "Authorization": "Bearer " + token
}

response = requests.get(url, headers=headers)

data = response.json()
print(data)

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

bear_uri = 'spotify:artist:2ifvIECHAlEgPMBuBOJ0lG'

credentials = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
spotify = spotipy.Spotify(client_credentials_manager=credentials)

results = spotify.artist_albums(bear_uri, album_type='album')
albums = results['items']
while results['next']:
    results = spotify.next(results)
    albums.extend(results['items'])

for album in albums:
    print(album['name'])

