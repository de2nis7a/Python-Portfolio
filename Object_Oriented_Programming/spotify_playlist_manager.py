# FILE: spotify_playlist_manager.py
# CONCEPT: Object-Oriented Programming (OOP) - List Management and Data Aggregation
# DEMONSTRATES: List manipulation (add, remove, insert) and complex aggregation 
#               (calculating total duration by separating minutes and seconds).

class Song:
    
    def __init__(self, title, album, duration, artist):
        self.title = title
        self.album = album
        # Store duration as a float (e.g., 3.50 is 3 minutes 30 seconds)
        self.duration = float(duration)
        self.artist = artist
        
    def __str__(self):
        # Format the duration to two decimal places
        return f"{self.title} by {self.artist} have {self.duration:.2f} minutes in the album {self.album}"
        
class Playlist:
    
    def __init__(self, title):
        self.title = title
        # songs should be an instance attribute, not a class attribute
        self.songs = []
    
    def add_song(self, song):
        if song not in self.songs:
            self.songs.append(song)
        
    def remove_song(self, song):
        if song in self.songs:
            self.songs.remove(song)
        
    def re_order(self, song, index):
        if song in self.songs:
            self.remove_song(song)
            # index - 1 to convert 1-based index to 0-based
            self.songs.insert(index - 1, song) 
            # NOTE: Removed the redundant self.add_song(song) call as it was already added by insert

    def duration(self):
        total_min = 0
        total_sec = 0
        
        for song in self.songs:
            # Separate minutes (integer part) and seconds (decimal part)
            minutes = int(song.duration)
            seconds_decimal = song.duration - minutes 
            
            total_min += minutes
            # Convert decimal seconds (e.g., 0.50) into true seconds (30)
            total_sec += round(seconds_decimal * 100) 
            
        # Convert total seconds into extra minutes
        extra_minutes = total_sec // 60
        remaining_seconds = total_sec % 60
        
        total_minutes = total_min + extra_minutes + remaining_seconds / 100
        
        return f"{total_minutes:.2f}"
            
    def __str__(self):
        output = f"The songs from the playlist {self.title} are: \n"
        for song in self.songs:
            output += f"- {song} \n"
        output += f"Having a total duration of {self.duration()} minutes."
        return output
            
def test_songs():
    # Durations are interpreted as MM.SS (e.g., 3.50 is 3 min 50 sec)
    song1 = Song("Leja", "Janc", 3.50, "Lui") # 3 min, 50 sec
    print(song1)
    song2 = Song("Qaj", "Cllevio", 4.20, "44") # 4 min, 20 sec
    song3 = Song("Mei", "gio", 4.20, "Andi") # 4 min, 20 sec
    
    playlist = Playlist("LOOVE")
    
    playlist.add_song(song1)
    playlist.add_song(song2)
    playlist.add_song(song3)
    
    # Re-order song2 to index 1 (the first position)
    playlist.re_order(song2, 1)

    print(playlist)

if __name__ == "__main__":
    test_songs()
