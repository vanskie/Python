def make_album(artist, album_title, number_songs = None):
    """Returns the given album info in a dictionary"""

    result = {}

    if number_songs != None:
        result['title'] = album_title.title()
        result['artist'] = artist.title()
        result['songs'] = number_songs
    else:
        result['title'] = album_title.title()
        result['artist'] = artist.title()

    return result

print(make_album(artist = 'jimi hendrix', album_title = 'johny b. good',\
number_songs = 5))
print(make_album(artist = 'red hot chili peppers',\
album_title = 'blood sugar sex magic'))
print(make_album(artist = 'red hot chili peppers',\
album_title = 'californication', number_songs = 18))

