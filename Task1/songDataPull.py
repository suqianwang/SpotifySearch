import sys
import spotipy
import time
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

#create list of playlist ids
with open('workingPlaylists.txt') as f:
	lines = [line.rstrip() for line in open('workingPlaylists.txt')]

#create output file
outfile = open("songData.txt","w")

#used to delay so the API doesn't cut requests
delay_count = 0;

#iterate across playlist ids and store song data to file
for playlist in range(len(lines)):
	#for finding problem ids
	if(playlist==0):
		playlist_num=0
	print(playlist_num, lines[playlist_num])
	outfile.write(str(sp.user_playlist_tracks('spotify', playlist_id=lines[playlist_num])))
	delay_count+=1
	if(delay_count == 200):
		time.sleep(5)
		delay_count = 0
	playlist_num+=1

outfile.close()
