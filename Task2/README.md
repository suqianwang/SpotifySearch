Directions for running Solr and importing Song Data

1. Download Solr: http://www.apache.org/dyn/closer.lua/lucene/solr/7.2.1
2. Go to the downloaded folder: solr-7.2.1/bin
3. Terminal: ./solr start
4. browser: http://localhost:8983/solr
5. Download the song data files at https://drive.google.com/file/d/1dObUNCUGYIc2OGvmjrhnYhOn3q0AgAjQ/view and extract in solr-7.2.1/bin
6. The filepath to the JSON files should be solr-7.2.1/bin/songsData/songsData
7. Download 'solrimport.sh' in the Task2 folder of this github and copy to solr-7.2.1/bin
8. In solr-7.2.1/bin, run './solr create -c SpotifyProject'
9. Run solrimport.sh using './solrimport.sh'. This is a script that I made to import all the song data, as trying to import them all at once throws an "Argument list too long" error. This will take about 8 minutes to run.
10. If you receive any errors, make sure that the filepaths for the JSON files are correct and files are in the correct directories. If all else fails, open the shell file in notepad and run the commands manually
11. After running, a core named 'SpotifyProject' should appear in the 'Core Admin' panel in the Solr browser client with all of our song data

Here is a good reference for query syntax with Solr: http://www.solrtutorial.com/solr-query-syntax.html
