import sys
import glob
import logging

from PySide2.QtWidgets import QFileDialog, QListWidgetItem, QListWidget
from PySide2.QtCore import QTranslator as tr
import PySide2.QtCore

logger = logging.getLogger(__name__)


class BatchFileController:

    def __init__(self):
        self.track_list = []


