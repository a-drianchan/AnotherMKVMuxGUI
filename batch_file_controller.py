import sys
import glob
import logging
from events import Events
from pymkv import MKVFile as MKVFile

from PySide2.QtWidgets import QFileDialog, QListWidgetItem, QListWidget
from PySide2.QtCore import QTranslator as tr
import PySide2.QtCore

from pymkv_wrapper import PymkvWrapper


logger = logging.getLogger(__name__)


class BatchFileController:

    def __init__(self):
        self._source_1_list = []
        self._source_2_list = []
        self.events = Events()

        self._user_settings_1 = []
        self._user_settings_2 = []

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

    def generate_item(self, mkv_path: str, list_widget: QListWidget):

        track_list = PymkvWrapper.process_file(str)
        for track in track_list:

            track_name = "N/A"
            track_type = track._track_type

            if track.track_name is not None:
                track_name = track.track_name

            track_item = QListWidgetItem("Track Name: " + track_name + " | " + "Type: " + track_type)
            track_item.setFlags(track_item.flags() | PySide2.QtCore.Qt.ItemFlag.ItemIsUserCheckable)
            track_item.setFlags(track_item.flags() | PySide2.QtCore.Qt.ItemFlag.ItemIsEnabled)
            track_item.setCheckState(PySide2.QtCore.Qt.CheckState.Unchecked)

            list_widget.addItem(track_item)

    def batch_mux(self):
        pass
