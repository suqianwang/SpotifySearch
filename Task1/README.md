```playlistPull.py``` pulls playlist data from Spotify playlist. This is using the spotipy library to utilize Spotify's developer API. The outputs of the run are stores in ```spotifyPlaylists.txt``` and ```morePlaylists.txt```.

```parser.cpp``` extract the playlist ID from the playlist data we crawled. The outputs of the run are stores in ```playlist_id.txt``` and ```morePlaylistIDs.txt```.

```songDataPull.py``` do deep crawling on ```spotifyPlaylists.txt``` and ```morePlaylists.txt```. The outputs are stored in the following link:

https://drive.google.com/file/d/1BPyEgXSKvPw41D8EdxXoMQLoovVK7pnd/view?usp=sharing

https://drive.google.com/file/d/1XBIjahHpi7mPAbKokww5XPdWKO0FYyqZ/view?usp=sharing

***need to separate each song's information***

### Modified

```workingPlaylists.txt``` contains all working playlists IDs we crawled so far.

```songDataPoll.py``` do deep crawling on ```workingPlaylists.txt```.

```pysplitter``` split infomation of each individual song. The outputs are stored in the following link

https://drive.google.com/file/d/1dObUNCUGYIc2OGvmjrhnYhOn3q0AgAjQ/view?usp=sharing (131k documents)

