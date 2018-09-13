from urllib2 import *
import simplejson

query = raw_input("Search by song: ") #take input for song title
query = query.strip().replace(" ","*") #Account for spaces in query

#Need to change 'SpotifyProject'in the following line to whatever your core
#is named in Solr
solrLink = "http://localhost:8983/solr/SpotifyProject/select?q=track.name:\"" #song title search prefix
jsonwt = "*\"&wt=json" #song title search postfix to specify json format

#establish connection to the Solr DB
connection = urlopen(solrLink.strip() + query + jsonwt.strip()) #use strip to concatenate without white space
response = simplejson.load(connection) #get response from query
print response['response']['numFound'], "documents found." #print num docs found

#print all song names returned
for document in response['response']['docs']:
	print "  Name =", document['track.name'][0], " --- Artist:", document['track.artists.name'][0]
