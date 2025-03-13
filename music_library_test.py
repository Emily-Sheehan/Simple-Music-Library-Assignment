from music_Library import *

#examples on how its used 

#creating a library
library = MusicLibrary()

#creating artists and songs
artist1 = Artist("Radiohead", "Alternative")               #creating artist using Artist Class
artist2 = Artist("The Cranberries", "Rock")
artist3 = Artist("Pink Floyd", "Classic Rock")

media1 = Media("Creep","3:58")
media2 = Media("Dreams", "4:31")
media3 = Media("Time", "7:02")
media4 = Media("Another Brick in the Wall", "3:10")

#using inheritance 
song1 = Song(media1.title, media1.duration, artist1.genre, artist1.name)
song2 = Song(media2.title, media2.duration, artist2.genre, artist2.name)
song3 = Song(media3.title, media3.duration, artist3.genre, artist3.name)
song4 = Song(media4.title, media4.duration, artist3.genre, artist3.name)

artist1.add_song(song1)
artist2.add_song(song2)
artist3.add_song(song2)  #adding incorrect song
artist3.remove_song(song2) #remove incorrect song
artist3.add_song(song3)
artist3.add_song(song4)

artist3.artist_discography()  #printing out Pink Floyd's Discography

#add artists and songs to library
library.add_artist(artist1)
library.add_artist(artist2)
library.add_song(song1)
library.add_song(song2)
library.add_song(song3)
library.add_song(song4)


#creating playlists
playlist = Playlist("Cool Songs")
playlist.add_song(song1)
playlist.add_song(song2)
playlist.add_song(song3)
playlist.add_song(song4)


#play all the playlist
print("\n")
playlist.play_all()

#remove song from playlist
playlist.remove_song(song4)

#play all playlist again 
print("\n")
playlist.play_all()

#playing just one song
print("\n")
song1.play()

#show all the songs in the library
print("\n")
library.print_all_songs()