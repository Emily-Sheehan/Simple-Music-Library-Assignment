#music library


#creating a media class to use as an example of inheritance with duration setter
class Media: 
    def __init__(self, title, duration):
        self._title = title     #encapsulation
        self._duration = duration  # Encapsulation 
    
    @property
    def title(self):                                                #encapsulation
        return self._title

    @property
    def duration(self):
        return self._duration



#creating a song Class 
class Song(Media):
    def __init__(self, title, duration, genre, artist):
        super().__init__(title, duration) #inherits title and duration from media
        self._genre = genre 
        self._artist = artist

    @property
    def genre(self):
        return self._genre

    @property
    def artist(self):
        return self._artist
    
    def play(self):
        print(f"Playing {self._title} by {self._artist}")

#creating a artist class
class Artist:
    def __init__(self, name, genre):
        self._name = name
        self._genre = genre 
        self._songs = []

    @property
    def name(self):
        return self._name
    
    @property
    def genre(self):
        return self._genre

    def add_song(self, song):
        self._songs.append(song)

    def remove_song(self, song):
        self._songs.remove(song)

    def artist_discography(self):
        print(f"Artist: {self._name}")
        print("Songs:")
        for song in self._songs:
            print(song.title)


#creating a playlist class
class Playlist:
    def __init__(self, name):
        self._name = name 
        self._songs = []

    @property
    def name(self):
        return self._name

    def add_song(self,song):
        self._songs.append(song)

    def remove_song(self, song):
        self._songs.remove(song)

    def play_all(self):
        print(self._name)
        for song in self._songs:
            song.play()

#creating the overall music library
class MusicLibrary:
    def __init__(self):
        self._songs = []
        self._artists = []
        self._playlists = []
    
    def add_song(self, song):
        self._songs.append(song)

    def add_artist(self, artist):
        self._artists.append(artist)

    def create_playlist(self, name):
        playlist = Playlist(name)
        self._playlists.append(playlist)
        playlist
    
    def print_all_songs(self):
        for song in self._songs:
            print(f"Title: {song.title}, Artist: {song.artist}, Genre: {song.genre}, Duration: {song.duration}")

