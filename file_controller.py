import sys
import glob
import logging

from PySide2.QtWidgets import QFileDialog, QListWidgetItem, QListWidget
from PySide2.QtCore import QTranslator as tr
import PySide2.QtCore

logger = logging.getLogger(__name__)


class FileController:

    def __init__(self):

        self._single_track_list = []

    def get_track(self, track_index: int):
        return self._single_track_list[track_index]

    def generate_item(self, track_list, list_widget: QListWidget):
        """
        Generate an QListWidgetItem and append it to a QListWidget
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


    @staticmethod
    def open_dialog_for_file():
        """
            Function wrapper to open file dialogs for selecting mkv files
        :return: a list of selected files
        """
        dialog = QFileDialog()
        dialog.setNameFilter("MKV files (*.mkv)")
        logger.debug("opening dialog")
        if dialog.exec_():
            file_names = dialog.selectedFiles()

            for file in file_names:
                logger.debug(file + " found")

        if file_names is not None:
            return file_names

    @staticmethod
    def open_dialog_for_directory():
        """
            Function wrapper to open file dialogs for selecting mkv files
        :return: a list of selected files
        """
        extensions = ["/*.mkv", "/*.ass", "/*.srt", "/*.flac", "/*.ac3"]
        file_list = []

        dialog = QFileDialog()
        dialog.setFileMode(QFileDialog.DirectoryOnly)
        if dialog.exec_():
            directory_name = dialog.selectedFiles()
            logger.debug(directory_name)
            for extension in extensions:
                logger.debug("Searching for " + extension)
                file_list.extend(glob.glob(directory_name[0] + extension))

            for file in file_list:
                logger.info(file + "found")

            return file_list

    @staticmethod
    def open_dialog_for_directory_name():
        """
            Function wrapper to open file dialogs and return name of the path
        :return: a list of selected files
        """
        extensions = ["/*.mkv", "/*.ass", "/*.srt", "/*.flac", "/*.ac3"]
        file_list = []

        dialog = QFileDialog()
        dialog.setFileMode(QFileDialog.DirectoryOnly)
        if dialog.exec_():
            directory_name = dialog.selectedFiles()
            return directory_name[0]

