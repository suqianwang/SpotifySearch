import sys
import spotipy
import time
import requests
import os
import io
import json
import spotipy.util as util
from spotipy.oauth2 import SpotifyClientCredentials

#Need to enter the following in terminal prior to running. Proper syntax to run is 'python songDataPoll.py <yourspotifyusername>'
# export SPOTIPY_CLIENT_ID='956b72a6c3244f47a96e524ea22d9a1b'
# export SPOTIPY_CLIENT_SECRET='86331697946f499fb23419d1ee7b918e'

# copy the URL of the redirect window
# nkm5oxrhxekr1xbw4w4k2u0hg
# get username
username = sys.argv[1]
scope = 'user-library-read'

# request user login
token = util.prompt_for_user_token(username, scope, redirect_uri = 'https://example.com/callback/')

# create spotify object
spotifyObject = spotipy.Spotify(auth=token)

# need credentials manager to access other users' playlists
client_credentials_manager = SpotifyClientCredentials()
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

#create list of playlist ids
with open('C:/cygwin64/home/Jake/SpotifyCrawl/workingPlaylists.txt') as f:
	lines = [line.rstrip() for line in f]

#used to delay so the API doesn't cut requests
delay_count = 0;

#iterate across playlist ids and store song data to file
allplaylists = {}
allPlaylistArray = []
for playlist in range(len(lines)):

	#for finding problem ids
	if(playlist==0):
		playlist_num=0
	print(playlist_num, lines[playlist_num])
	playlistSongs = []
	try:
		if playlist_num <= 1299:
			playlistSongs = sp.user_playlist_tracks('spotify', playlist_id=lines[playlist_num])['items']
		else:
			playlistSongs = sp.user_playlist_tracks('cabal76', playlist_id=lines[playlist_num])['items']	
		playlistDict = {'playlist': playlistSongs}
		allPlaylistArray.append(playlistDict)		
		delay_count+=1
		if(delay_count == 200):
			time.sleep(5)
			delay_count = 0
		playlist_num+=1
	except requests.exceptions.HTTPError:
		print(playlist_num, lines[playlist_num], 'HTTPerror')
	except spotipy.client.SpotifyException:
		print(playlist_num, lines[playlist_num], 'SpotifyError')
		playlist_num+=1

allplaylists = {'item': allPlaylistArray}
filename = "C:/cygwin64/home/Jake/SpotifyCrawl/allPlaylist.json"
outfile = open(filename,"w+")
outfile.write(json.dumps(allplaylists, sort_keys=False, indent=4, separators=(',', ': ')))
outfile.close()
