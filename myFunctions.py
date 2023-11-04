import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())


def get_artist_id():
    name = input("\nEnter the name of an artist: ")
    search = spotify.search(name, 1, 0, "artist")
    artist = search['artists']['items'][0]
    artist_id = artist['id']
    return artist_id


def list_artist_albums():
    id = get_artist_id()
    results = spotify.artist_albums(id, album_type='album')
    albums = results['items']

    while results['next']:
        results = spotify.next(results)
        albums.extend(results['items'])

    for album in albums:
        print(album['name'] + " (" + album['release_date'][:4] + ")")


def list_top_tracks():
    id = get_artist_id()
    results = spotify.artist_top_tracks(id)

    rank = 1
    for track in results['tracks'][:10]:
        print(f'{rank}' + '. ' + track['name'])
        rank += 1
