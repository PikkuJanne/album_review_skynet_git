from PyQt5.QtCore import QObject, pyqtProperty, pyqtSlot, pyqtSignal
from ars_ver2 import RockAlbumReviewGenerator, PopAlbumReviewGenerator

class AlbumReviewHandler(QObject):
    reviewChanged = pyqtSignal()

    def __init__(self):
        super().__init__()
        self._band_name = ""
        self._album_name = ""
        self._is_rock_album = False
        self._review = ""
        self.rock_album_review_generator = RockAlbumReviewGenerator()
        self.pop_album_review_generator = PopAlbumReviewGenerator()

    @pyqtProperty(str, notify=reviewChanged)
    def band_name(self):
        return self._band_name

    @pyqtProperty(str, notify=reviewChanged)
    def album_name(self):
        return self._album_name

    @pyqtProperty(bool, notify=reviewChanged)
    def is_rock_album(self):
        return self._is_rock_album

    @pyqtProperty(str, notify=reviewChanged)
    def review(self):
        return self._review

    @pyqtSlot(str)
    def generate_review(self, lead_songs_text):
        lead_songs = lead_songs_text.strip().split('\n')
        if self._is_rock_album:
            review = self.rock_album_review_generator.generate_review(self._album_name, self._band_name, lead_songs)
        else:
            review = self.pop_album_review_generator.generate_review(self._album_name, self._band_name, lead_songs)
        
        self._review = review
        self.reviewChanged.emit()
