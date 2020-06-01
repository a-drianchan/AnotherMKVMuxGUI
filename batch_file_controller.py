import sys
import glob
import logging
from events import Events

from PySide2.QtWidgets import QFileDialog, QListWidgetItem, QListWidget
from PySide2.QtCore import QTranslator as tr
import PySide2.QtCore

logger = logging.getLogger(__name__)


class BatchFileController:

    def __init__(self):
        self._source_1_list = []
        self._source_2_list = []
        self.events = Events()

    @property
    def source_1_list(self):
        return self._source_1_list

    @source_1_list.setter
    def source_1_list(self, file_list):
        self._source_1_list = file_list
        self.events.on_batch_list_1_update()

    @property
    def source_2_list(self):
        return self._source_2_list

    @source_2_list.setter
    def source_2_list(self, file_list):
        self._source_2_list = file_list
        self.events.on_batch_list_2_update()

    def generate_item(self, file_list, list_widget: QListWidget, list: int):

        if list == 1:
            self._source_1_list.extend(file_list)
        elif list == 2:
            self._source_2_list.extend(file_list)

        for file in file_list:
            item = QListWidgetItem(file)
            list_widget.addItem(item)
