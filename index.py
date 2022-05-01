import rumps
import sys
from tk import Window
from PyQt5.Qt import *


class AwesomeStatusBarApp(rumps.App):
    def __init__(self, name):
        super(AwesomeStatusBarApp, self).__init__(
            icon='index.png', title=name, name=name)

    @rumps.clicked("Ask")
    def prefs(self, _):
        app = QApplication(sys.argv)
        window = Window()
        window.show()
        sys.exit(app.exec_())


if __name__ == "__main__":
    AwesomeStatusBarApp("Baidu App").run()
