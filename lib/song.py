class Song:
    count = 0
    artists = []
    genres = []
    genre_count = {}
    artist_count = {}


    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre
        self.add_song_to_count()
        self.add_to_genres(genre)
        self.add_to_artists(artist)
        
    @classmethod
    def add_song_to_count(cls):
        cls.count += 1
        
    @classmethod
    def add_to_genres(cls, genre):
        if genre not in cls.genres:
            cls.genres.append(genre)
            cls.genre_count[genre] = 1
        else:
            cls.genre_count[genre] += 1

    @classmethod
    def add_to_artists(cls, artist):
        if artist not in cls.artists:
            cls.artists.append(artist)
            cls.artist_count[artist] = 1
        else:
            cls.artist_count[artist] += 1


song = Song("lily", "nana", "pop")
song = Song("nana", "lily", "rock")
print(Song.count)
print(Song.artists)
print(Song.genres)
print(Song.artist_count)
print(Song.genre_count)


    