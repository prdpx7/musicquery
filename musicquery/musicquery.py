"""
A Python packge which returns song_path after matching given query
with all existing songs in music_dir
"""
import re
import os
import random
import tinytag
class MusicQuery(object):
    """
    def __init__(self, music_dir, title=None, artist=None, genre=None)
     attrs: music_dir,artist,genre,status,song_path,error,all_song_path_list
    1. for valid matched song
            'status':'ok',
            'song_path':'/home/username/Music/starboy.mp3'
    2. for invalid song query
            'status':'unable to find song_path for given args',
            'error':'music_dir does not exists'
    """
    def _clean_tag(self, tag):
        if tag is None:
            return "Unknown"
        return tag

    def _matched_song_with_title(self, path):
        title = tinytag.TinyTag.get(path).title
        # title maybe none if tag is not present
        if title and re.search(r'%s'%self.title, title, re.IGNORECASE):
            return True
        return False

    def _matched_song_with_artist(self, path):
        artist = tinytag.TinyTag.get(path).artist
        if artist and re.search(r'%s'%self.artist, artist, re.IGNORECASE):
            return True
        return False

    def _matched_song_with_genre(self, path):
        genre = tinytag.TinyTag.get(path).genre
        if genre and re.search(r'%s'%self.genre, genre, re.IGNORECASE):
            return True
        return False

    def _set_tags(self):
        title = tinytag.TinyTag.get(self.song_path).title
        self.title = self._clean_tag(title)
        artist = tinytag.TinyTag.get(self.song_path).artist
        self.artist = self._clean_tag(artist)
        genre = tinytag.TinyTag.get(self.song_path).genre
        self.genre = self._clean_tag(genre)

    def __init__(self, music_dir, title=None, artist=None, genre=None):
        self.music_dir = os.path.expanduser(music_dir)
        self.title = title
        self.artist = artist
        self.genre = genre
        self.status = 'ok'
        self.song_path = None
        self.error = None
        self.all_song_path_list = []
        if not os.path.exists(self.music_dir):
            self.status = 'unable to find song_path'
            self.error = 'invalid path `%s`'%(self.music_dir)
            return None
        else:
            self.all_song_path_list = map(lambda x: self.music_dir + x, os.listdir(self.music_dir))
        if self.genre:
            self.all_song_path_list = [path for path in self.all_song_path_list
                                       if self._matched_song_with_genre(path)]
        if self.title:
            self.all_song_path_list = [path for path in self.all_song_path_list
                                       if self._matched_song_with_title(path)]
            if self.artist:
                self.song_path = filter(self._matched_song_with_artist, self.all_song_path_list)

        if self.artist:
            self.all_song_path_list = [path for path in self.all_song_path_list
                                       if self._matched_song_with_artist(path)]
        if self.song_path is None or isinstance(self.song_path, list):
            if self.all_song_path_list:
                song_list_len = len(self.all_song_path_list) - 1
                self.song_path = self.all_song_path_list[random.randint(0, song_list_len)]
                self._set_tags()
            else:
                self.status = 'unable to find song_path'
                self.error = 'can not find any matching song tags with given args'

    def __str__(self):
        return  str({'artist':self.artist,
                     'title':self.title,
                     'genre':self.genre,
                     'song_path':self.song_path,
                     'status':self.status,
                     'error':self.error,
                    })
