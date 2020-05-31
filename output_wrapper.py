import sys
import logging
import PySide2.QtGui

logger = logging.getLogger()

"""
Class used to direct the std output to a Qt QTestEdit object
"""
class OutputWrapper(object):
    def __init__(self, edit):
        self.out = sys.stdout
        self.textEdit = edit

    def write(self, message):
        self.textEdit.moveCursor(PySide2.QtGui.QTextCursor.End)
        self.out.write(message)
        self.textEdit.append(message)

    def flush(self):
        self.out.flush()
        self.out.flush()
