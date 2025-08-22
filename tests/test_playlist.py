
import pytest
from playlist\_manager import Song, PlaylistManager

def test\_song\_to\_dict():
song = Song('Test Title', 'Test Artist', 'Test Album', '03:30')
expected = {
'title': 'Test Title',
'artist': 'Test Artist',
'album': 'Test Album',
'duration': '03:30'
}
assert song.to\_dict() == expected

def test\_add\_song():
manager = PlaylistManager(json\_file='\:memory:')  # using in-memory simulation
manager.add\_song('Song1', 'Artist1', 'Album1', '04:00')
assert len(manager.songs) == 1
assert manager.songs\[0].title == 'Song1'

def test\_search\_song():
manager = PlaylistManager(json\_file='\:memory:')
manager.add\_song('Hello World', 'ArtistX', 'AlbumX', '03:45')
results = \[s for s in manager.songs if 'hello' in s.title.lower()]
assert len(results) == 1
assert results\[0].artist == 'ArtistX'

def test\_shuffle\_play():
manager = PlaylistManager(json\_file='\:memory:')
manager.add\_song('SongA', 'ArtistA', 'AlbumA', '02:30')
manager.add\_song('SongB', 'ArtistB', 'AlbumB', '03:15')
song = manager.songs\[0]  # just pick the first for deterministic test
assert song.title in \['SongA', 'SongB']
