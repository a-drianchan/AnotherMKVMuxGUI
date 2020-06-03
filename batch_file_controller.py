import sys
import glob
import logging
import threading

from events import Events
from pymkv import MKVFile as MKVFile

from PySide2.QtWidgets import QFileDialog, QListWidgetItem, QListWidget
from PySide2.QtCore import QTranslator as tr
import PySide2.QtCore

from pymkv_wrapper import PymkvWrapper
from gui_helper import GuiHelper

logger = logging.getLogger(__name__)


class BatchFileController:

    def __init__(self):
        self._source_1_list = []
        self._source_2_list = []
        self.events = Events()

        self._tracks_1 = []
        self._tracks_2 = []

        self._user_settings_1 = []
        self._user_settings_2 = []

        self.output_directory = None

        self.events.on_batch_list_update += self.generate_item

    @property
    def source_1_list(self):
        return self._source_1_list

    @source_1_list.setter
    def source_1_list(self, file_list):
        self._source_1_list = file_list
        self.events.on_batch_list_update(file_list, 1)

    @property
    def source_2_list(self):
        return self._source_2_list

    @source_2_list.setter
    def source_2_list(self, file_list):
        self._source_2_list = file_list
        self.events.on_batch_list_update(file_list, 2)

    @property
    def user_setting_1(self):
        return self._user_settings_1

    @property
    def user_setting_2(self):
        return self._user_settings_2

    def generate_item(self, file_list, list_num: int):

        if list == 1:
            self._source_1_list.extend(file_list)
        elif list == 2:
            self._source_2_list.extend(file_list)

        for file in file_list:
            item = QListWidgetItem(file)
            self.events.batch_file_item_generated(item, list_num)

    def generate_track_item(self, ref_num: int):
        """
        Generate the track list for the two input directories with the first file in the list
        :return:
        """

        if len(self._source_1_list) != 0 and ref_num == 1:

            self._tracks_1 = PymkvWrapper.process_file(self._source_1_list[0])

            #TODO turn item generate into GUI helper
            for track in self._tracks_1:

                track_name = "N/A"
                track_type = track._track_type

                if track.track_name is not None:
                    track_name = track.track_name

                track_item_1 = QListWidgetItem("Track Name: " + track_name + " | " + "Type: " + track_type)
                track_item_1.setFlags(track_item_1.flags() | PySide2.QtCore.Qt.ItemFlag.ItemIsUserCheckable)
                track_item_1.setFlags(track_item_1.flags() | PySide2.QtCore.Qt.ItemFlag.ItemIsEnabled)
                track_item_1.setCheckState(PySide2.QtCore.Qt.CheckState.Unchecked)

                self.events.ref_tracks_generated(self._source_1_list[0], track_item_1, 1)

        if len(self._source_2_list) != 0 and ref_num == 2:

            self._tracks_2 = PymkvWrapper.process_file(self._source_2_list[0])
            # TODO turn item generate into GUI helper
            for track in self._tracks_2:

                track_name = "N/A"
                track_type = track._track_type

                if track.track_name is not None:
                    track_name = track.track_name

                track_item_2 = QListWidgetItem("Track Name: " + track_name + " | " + "Type: " + track_type)
                track_item_2.setFlags(track_item_2.flags() | PySide2.QtCore.Qt.ItemFlag.ItemIsUserCheckable)
                track_item_2.setFlags(track_item_2.flags() | PySide2.QtCore.Qt.ItemFlag.ItemIsEnabled)
                track_item_2.setCheckState(PySide2.QtCore.Qt.CheckState.Unchecked)

                self.events.ref_tracks_generated(self._source_2_list[0], track_item_2, 2)

    def gather_all_selected_track(self, list_1: QListWidget, list_2: QListWidget):

        self._user_settings_1 = []
        self._user_settings_2 = []
        logger.debug("Gathering selected tracks")

        for index in range(list_1.count()):

            item = list_1.item(index)
            if item.checkState() == PySide2.QtCore.Qt.Checked:
                self._user_settings_1.append(index)

        logger.debug("Reference 1 Tracks : " + str(self._user_settings_1).strip('[]'))

        for index in range(list_2.count()):

            item = list_2.item(index)
            if item.checkState() == PySide2.QtCore.Qt.Checked:
                self._user_settings_2.append(index)

        logger.debug("Reference 2 Tracks : " + str(self._user_settings_2).strip('[]'))

    def batch_mux_files(self,):
        batch_mux_thread = threading.Thread(
            PymkvWrapper.batch_mux_files(self.source_1_list, self.source_1_list,
                                         self.user_setting_1, self.user_setting_2,
                                         self.output_directory, ""))
        batch_mux_thread.start()


    def clear_all(self):
        self._source_1_list = []
        self._source_2_list = []
        self._tracks_1 = []
        self._tracks_2 = []
        self._user_settings_1 = []
        self._user_settings_2 = []
        self.events.clear_all()
