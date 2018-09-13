import sys
import spotipy
import spotipy.util as util
from spotipy.oauth2 import SpotifyClientCredentials

#Need to enter the following in terminal prior to running. Proper syntax to run is 'python playlistPull.py <yourspotifyusername>'
# export SPOTIPY_CLIENT_ID='7b00e2e252244c9789e862e391de1306'
# export SPOTIPY_CLIENT_SECRET='dcbbe3b243c549578dbca789858bd222'
# export SPOTIPY_REDIRECT_URI='http://google.com/'

# get username
username = sys.argv[1]
scope = 'user-library-read'

# request user login
token = util.prompt_for_user_token(username, scope)

# create spotify object
spotifyObject = spotipy.Spotify(auth=token)

# need credentials manager to access other users' playlists
client_credentials_manager = SpotifyClientCredentials()
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

playlists = sp.user_playlists('spotify')
while playlists:
    for i, playlist in enumerate(playlists['items']):
        print("%4d %s %s" % (i + 1 + playlists['offset'], playlist['uri'],  playlist['name']))
    if playlists['next']:
        playlists = sp.next(playlists)
    else:
        playlists = None
