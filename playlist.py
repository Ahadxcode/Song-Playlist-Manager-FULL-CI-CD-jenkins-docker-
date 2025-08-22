import json
import csv
import random

class Song:
    def __init__(self, title, artist, album, duration):
        self.title = title
        self.artist = artist
        self.album = album
        self.duration = duration  # minutes:seconds

    def to_dict(self):
        return {
            "title": self.title,
            "artist": self.artist,
            "album": self.album,
            "duration": self.duration
        }

class PlaylistManager:
    def __init__(self, json_file="playlist.json", csv_file="playlist.csv"):
        self.json_file = json_file
        self.csv_file = csv_file
        self.songs = []
        self.load_from_json()

    def add_song(self, title, artist, album, duration):
        self.songs.append(Song(title, artist, album, duration))
        self.save_to_json()

    def list_songs(self):
        if not self.songs:
            print("No songs in playlist.")
            return
        print("\nPlaylist:")
        print("Title | Artist | Album | Duration")
        for s in self.songs:
            print(f"{s.title} | {s.artist} | {s.album} | {s.duration}")

    def search_songs(self, keyword):
        results = [s for s in self.songs if keyword.lower() in s.title.lower() or keyword.lower() in s.artist.lower()]
        if results:
            print("\nSearch Results:")
            for s in results:
                print(f"{s.title} | {s.artist} | {s.album} | {s.duration}")
        else:
            print("No matches found.")

    def shuffle_play(self):
        if not self.songs:
            print("Playlist is empty.")
            return
        song = random.choice(self.songs)
        print(f"Now playing: {song.title} by {song.artist} ({song.duration})")

    def save_to_json(self):
        with open(self.json_file, "w") as f:
            json.dump([s.to_dict() for s in self.songs], f, indent=4)

    def load_from_json(self):
        try:
            with open(self.json_file, "r") as f:
                data = json.load(f)
                self.songs = [Song(**song) for song in data]
        except FileNotFoundError:
            self.songs = []

    def save_to_csv(self):
        with open(self.csv_file, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["Title", "Artist", "Album", "Duration"])
            for s in self.songs:
                writer.writerow([s.title, s.artist, s.album, s.duration])


if __name__ == "__main__":
    manager = PlaylistManager()

    while True:
        print("\nMusic Playlist Manager")
        print("1. Add Song")
        print("2. List Songs")
        print("3. Search Songs")
        print("4. Shuffle Play")
        print("5. Export to CSV")
        print("6. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            title = input("Song title: ")
            artist = input("Artist: ")
            album = input("Album: ")
            duration = input("Duration (mm:ss): ")
            manager.add_song(title, artist, album, duration)

        elif choice == "2":
            manager.list_songs()

        elif choice == "3":
            keyword = input("Enter keyword (title/artist): ")
            manager.search_songs(keyword)

        elif choice == "4":
            manager.shuffle_play()

        elif choice == "5":
            manager.save_to_csv()
            print("Playlist exported to CSV!")

        elif choice == "6":
            print("Goodbye!")
            break

        else:
            print("Invalid choice.")
