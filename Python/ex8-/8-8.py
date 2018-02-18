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


flag = True

print('You can write \'q\' whenever in the program to quit!')
while flag:
    
    if flag == False:
        break
         
    prompt_artist = input('Enter an artist name: ')
    if prompt_artist == 'q':
        flag = False
        continue
    prompt_title = input('Enter an album name: ')
    if prompt_title == 'q':
        flag = False
        continue
    songs = input('Would you like to add how many songs are in the album\
    (this is completely optional by the way): (y/n)')
    if songs == 'y':
        songs = input('How many songs are in {}?: '.format(prompt_title))
    if songs == 'n':
        songs = None 
    if songs == 'q':
        flag = False
        continue
    
    #Feeding information to the function
    #Giving arguments to the parameters
    print(make_album(artist = prompt_artist, album_title = prompt_title,\
    number_songs = songs))


    
