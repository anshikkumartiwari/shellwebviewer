import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QStatusBar, QToolBar
from PyQt6.QtWebEngineWidgets import QWebEngineView
from PyQt6.QtCore import QUrl
from PyQt6.QtGui import QIcon, QAction

class Browser(QMainWindow):
    def __init__(self, url):
        super().__init__()
        self.setWindowTitle("Shell Web Viewer")
        self.setWindowIcon(QIcon('/home/anshikkumartiwari/images/bashlogo2.png'))  # don't forget to chnage this path accordingly
        
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl(url))
        self.setCentralWidget(self.browser)
        
        self.status = QStatusBar()
        self.setStatusBar(self.status)
        
        self.browser.urlChanged.connect(self.update_status)
        self.browser.loadProgress.connect(self.update_progress)
        self.browser.loadFinished.connect(self.load_finished)
        
        self.create_toolbar()
        
        self.show()
    
    def update_status(self, url):
        self.status.showMessage(url.toString())
    
    def update_progress(self, progress):
        self.status.showMessage(f"Loading... {progress}%")
    
    def load_finished(self):
        self.status.showMessage("Loading complete")
    
    def create_toolbar(self):
        toolbar = QToolBar()
        self.addToolBar(toolbar)
        
        back_action = QAction("<<<", self)
        back_action.setShortcut("Alt+Left")
        back_action.triggered.connect(self.browser.back)
        toolbar.addAction(back_action)
        
        refresh_action = QAction("Refresh", self)
        refresh_action.setShortcut("Ctrl+R")
        refresh_action.triggered.connect(self.browser.reload)
        toolbar.addAction(refresh_action)
        
        forward_action = QAction(">>>", self)
        forward_action.setShortcut("Alt+Right")
        forward_action.triggered.connect(self.browser.forward)
        toolbar.addAction(forward_action)

if __name__ == "__main__":
    try:
        app = QApplication(sys.argv)
        app.setStyleSheet("""
            QMainWindow {
                background-color: #2E3440;
                color: #D8DEE9;
            }
            QStatusBar {
                background-color: #3B4252;
                color: #D8DEE9;
            }
            QWebEngineView {
                background-color: #2E3440;
            }
        """)
        
        if len(sys.argv) > 1:
            url = sys.argv[1]
            window = Browser(url)
            window.show()
            sys.exit(app.exec())
        else:
            print("No URL provided.")
    except Exception as e:
        print(f"An error occurred: {e}")
