Download ```solrimportv2.sh``` in the Task2 folder of this github and copy to solr-7.2.1/bin

Terminal: ```./solr start```

browser: http://localhost:8983/solr

In solr-7.2.1/bin, run ```./solr create -c SpotifyProject```

run ```./solrimportv2.sh```  This is a script to import all the song data

run ```python SimpleWindow.py``` to start the GUI for our application (songTitleSearch is intergrated with the SimpleWindow.py, therefore it is no longer needed)
