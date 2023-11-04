from myFunctions import *
import time

print('***********************************\n')
print('        Spotify API Search         ')
print('\n***********************************\n')

print('Welcome! This program is designed to utilize the Spotify Web API to display facts about music artists.')
print('Navigate this software by typing and entering the number of a menu option below.')

while True:
    print('\n\n--------------------------------')
    print('----------  MENU  --------------')
    print("1. View an artist's discography")
    print("2. See an artist's top 10 tracks")
    print('3. Quit')
    choice = input('Enter an option (1, 2, or 3): ')

    if choice == '1':
        list_artist_albums()
    if choice == '2':
        list_top_tracks()
    if choice == '3':
        break

    time.sleep(1)


print('\nThe program has ended')
