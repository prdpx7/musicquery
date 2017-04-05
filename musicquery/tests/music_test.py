import musicquery
from unittest import TestCase
import os
class TestMusic(TestCase):
    music_dir = '/musicquery/tests/test_music_library/'
    base_path = os.path.abspath('.')
    def test_all_songs(self):
        test_obj = musicquery.MusicQuery(music_dir=self.base_path+self.music_dir)
        songs_list = map(lambda song: self.base_path + self.music_dir + song, ['synth.mp3', 'twinkle.mp3'])
        self.assertTrue(test_obj.all_song_path_list, songs_list)
    def test_genre(self):
        test_obj = musicquery.MusicQuery(music_dir=self.base_path+self.music_dir, genre='simple')
        self.assertTrue(test_obj.song_path, self.base_path+self.music_dir+'twinkle.mp3')
