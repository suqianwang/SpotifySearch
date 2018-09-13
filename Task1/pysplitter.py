import re
import os
import json
import ast
from pprint import pprint

allfiles = os.listdir(r'C:\cygwin64\home\Jake\SpotifyCrawl\test')
allsongs = []
playlistnum = 1
test = 0
for file in allfiles:
    inputfile = open(r'C:\cygwin64\home\Jake\SpotifyCrawl\test' + '\\' + file)
    inputtext = inputfile.read()
    inputfile.close()
    currentsongs = re.findall(r"\'is_local.*?(\'track\':\ .*?\'added_at\'.*?})", inputtext)
    currentsongs = ['{{{0}, '.format(song) for song in currentsongs] # Format each song as a valid json
    if test == 756:
        print(file)
    if len(currentsongs) == 0:
        break
    elif playlistnum == 1:
        currentsongs.insert(0, '{\'items\': [{\'playlist\': [' + currentsongs.pop(0)) # Have each song be a playlist
    else:
        currentsongs.insert(0, ' {\'playlist\': [' + currentsongs.pop(0)) # Have each song be a playlist
    currentsongs.append(currentsongs.pop(-1)[:-2] + ']},')
    playlist = ""
    for song in currentsongs:
        playlist = playlist + song
    if playlistnum == 1:    
        allsongs.append(playlist)
        playlistnum = 2
    else:
        allsongs.append(allsongs.pop(0) + playlist)
    test += 1
allsongs.append(allsongs.pop(-1)[:-1] + ']}')
songnum = 0
print (len(allsongs))
with open('allSongsData.json', 'wt') as songfile:
    allplaylists = allsongs.pop(0)
    print (allplaylists)
    print("\n\n\n\n")
    parsed = eval(allplaylists)
        # print(parsed)
        # songfile.write(json.dumps(parsed, sort_keys=False, indent=4, separators=(',', ': ')))
        # songnum += 1