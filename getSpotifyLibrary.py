import httplib
import json
import sys

totalArgs = len(sys.argv)
if (totalArgs != 4):
    print "usage: getSpotifyPlaylist.py playListId userName secureToken"
    sys.exit()

def printItem(item):
    print item['track']['name'] + "~" + item['track']['artists'][0]['name'] + "~" + item['track']['album']['name'];
    return

firstPass = True
next = "/v1/users/" + sys.argv[2] + "/playlists/" + sys.argv[1]
while next:
    conn = httplib.HTTPSConnection("api.spotify.com")
    conn.putrequest("GET", next)
    conn.putheader('Authorization', 'Bearer ' + sys.argv[3])
    conn.endheaders()
    data = json.load(conn.getresponse())

    # The JSON response is structured differently for urls with parameters
    if (firstPass):
        for item in data['tracks']['items']:
            printItem(item)
        if (data['tracks']['next']):
            next = data['tracks']['next'][23:]
            firstPass = False
        else:
            sys.exit()
    else:
        for item in data['items']:
            printItem(item)
        if (data['next']):
            next = data['next'][23:]
        else:
            sys.exit()
