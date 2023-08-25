import sys
from PyQt5.QtCore import QUrl
from PyQt5.QtGui import QGuiApplication
from PyQt5.QtQml import QQmlApplicationEngine
from arh import AlbumReviewHandler

class AlbumReviewApp:
    def __init__(self):
        self.app = QGuiApplication(sys.argv)
        self.engine = QQmlApplicationEngine()

        self.album_review_handler = AlbumReviewHandler()

        self.engine.rootContext().setContextProperty("albumReviewHandler", self.album_review_handler)

        self.load_qml()
        sys.exit(self.app.exec_())

    def load_qml(self):
        print("Loading QML file...")
        self.engine.load(QUrl.fromLocalFile('ars.ui.qml'))
        
        # Check if the QML file has been loaded correctly
        if not self.engine.rootObjects():
            sys.exit(-1)

        # Get the root window object and show it
        window = self.engine.rootObjects()[0]
        window.show()

        print("Application Loaded Successfully!")

if __name__ == "__main__":
    print("Initializing Application...")
    AlbumReviewApp()
