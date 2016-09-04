# simple-spotify-export
Exports a spotify playlist to the following line output pattern per track: title~artist~album

####usage
./getSpotifyLibrary.py {playlistId} {userName} {OAuth Token}

####example
./getSpotifyLibrary.py 0WQ8DIncGbXBTp9OV4J9uO tkealamakia  BQCKbZSTKgvKIwlpChBAnWPCjUTrh--JXwGJCJO5ltufvy_sc-W41ZsHJvTgQqrgbFSSqSbp69NucfsUa1y-_ok0JISaWDHMJuySEheGvTgRFxl82FttjIVDHtlxlaVvOG00lUCnGzz3Q6I_oCRi0wheDkr7m8v6Cnk8Jb0U

The spotify api does not allow a full library api request so if you want to export all your saved tracks, you will need to create a mega playlist out of them.

To obtain an OAuth Token navigate to: https://developer.spotify.com/web-api/console/get-playlists/

Click on the 'GET OAUTH TOKEN' button, check the 'playlist-read-private' box and then click the 'REQUEST TOKEN' button.  You will be prompted to login.  Upon successful login you will now be presented with the token in the 'OAuth Token' field. As of this writing this token is valid for the duration of 1 hour.
