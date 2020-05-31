from events import Events
import logging

from PySide2.QtWidgets import QFileDialog, QListWidgetItem, QListWidget
from PySide2.QtCore import QTranslator as tr
import PySide2.QtCore

logger = logging.getLogger(__name__)


class FileController:

    def __init__(self):
        self.events = Events()
        self._single_track_list = []

    def get_track(self, track_index: int):
        return self._single_track_list[track_index]

    def generate_item(self, track_list, list_widget: QListWidget):
        """
        Generate an QListWidgetItem, enable checkboxes and append it to a QListWidget
        :param track_list:
        :param list_widget:
        :return:
        """
        self._single_track_list.extend(track_list)

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

    def clear_track_list(self):
        self._single_track_list = []
        self.events.onClear()


