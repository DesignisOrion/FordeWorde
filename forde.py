from PyQt5.QtWidgets import *
from PyQt5.QtGui import QKeySequence, QPalette, QColor
from PyQt5.QtCore import Qt


app = QApplication([])

# Force the theme style to be the same on all OSs:
app.setStyle("Fusion")

# Now use a palette to switch to dark colors:
palette = QPalette()
palette.setColor(QPalette.Window, QColor(53, 53, 53))
palette.setColor(QPalette.WindowText, Qt.white)
palette.setColor(QPalette.Base, QColor(25, 25, 25))
palette.setColor(QPalette.AlternateBase, QColor(53, 53, 53))
palette.setColor(QPalette.ToolTipBase, Qt.white)
palette.setColor(QPalette.ToolTipText, Qt.white)
palette.setColor(QPalette.Text, Qt.white)
palette.setColor(QPalette.Button, QColor(53, 53, 53))
palette.setColor(QPalette.ButtonText, Qt.white)
palette.setColor(QPalette.BrightText, Qt.red)
palette.setColor(QPalette.Link, QColor(42, 130, 218))
palette.setColor(QPalette.Highlight, QColor(42, 130, 218))
palette.setColor(QPalette.HighlightedText, Qt.black)
app.setPalette(palette)

# coding the text editor.

app.setApplicationName("Forde Worde")


text = QPlainTextEdit()



class MainWindow(QMainWindow):
    def closeEvent(self, e):
        if not text.document().isModified():
            return
        answer = QMessageBox.question(
            window, None,
            "You have unsaved changes. Save before closing?",
            QMessageBox.Save | QMessageBox.Discard | QMessageBox.Cancel
        )
        if answer & QMessageBox.Save:
            save()
        elif answer & QMessageBox.Cancel:
            e.ignore()
window = MainWindow()
window.setCentralWidget(text)
file_path = None

# file menu
menu = window.menuBar().addMenu("&File")
open_action = QAction("&Open")


def open_file():
    global file_path
    path = QFileDialog.getOpenFileName(window, "Open")[0]
    if path:
        text.setPlainText(open(path).read())
        file_path = path

# Created by DesignIsOrion (2020)


open_action.triggered.connect(open_file)
open_action.setShortcut(QKeySequence.Open)
menu.addAction(open_action)

save_action = QAction("&Save")


def save():
    if file_path is None:
        save_as()
    else:
        with open(file_path, "w") as f:
            f.write(text.toPlainText())
        text.document().setModified(False)


save_action.triggered.connect(save)
save_action.setShortcut(QKeySequence.Save)
menu.addAction(save_action)

save_as_action = QAction("Save &As...")

# Created by DesignIsOrion (2020)


def save_as():
    global file_path
    path = QFileDialog.getSaveFileName(window, "Save As")[0]
    if path:
        file_path = path
        save()


save_as_action.triggered.connect(save_as)
menu.addAction(save_as_action)

close = QAction("&Close")
close.triggered.connect(window.close)
menu.addAction(close)


# henry Bot menu
'''
def henry_app():
    listener = sr.Recognizer()
    engine = pyttsx3.init()
    engine.say('I am Henry The Butler')
    engine.say('Start speaking and I will begin typing right away.')
    engine.runAndWait()


    try:
        # recording from mic and recording
        with sr.Microphone() as source:
                
            # Infoming user that Henry is listening.
            print('Henry is listening...')
            voice = listener.listen(source)
            # functions for voice to text
            command = listener.recognize_google(voice)
                
            # dictate if Henry is there or not.
            # This will allow it to be called only when saying Henry
            command = command.lower()
            if 'Henry' in command:
                    command = command.replace('henry', '')
                    print(command)
    except:
        pass 
                
henry_menu = window.menuBar().addMenu("&Henry")
henry_action = QAction("&Henry")
henry_menu.addAction(henry_action)

henry_action.triggered.connect(henry_app)

'''
# help menu

help_menu = window.menuBar().addMenu("&Help")
about_action = QAction("&About")
help_menu.addAction(about_action)

# Created by DesignIsOrion (2020)

# About dialog box
def show_about_dialog():
    text = "<center>" \
            "<img src=logo.png>" \
           "<h1>Forde Worde</h1>" \
           "&#8291;" \
           "<p>Version 2.0<br/>" \
           "</center>" \
           "Copyright &copy; 2021 DesignIsOrion.com</p>"
    QMessageBox.about(window, "About Forde Worde v2", text)


about_action.triggered.connect(show_about_dialog)




window.show()
app.exec_()