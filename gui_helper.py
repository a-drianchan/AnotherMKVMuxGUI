from PySide2.QtWidgets import QListWidgetItem, QListWidget
from pymkv import MKVTrack
from file_controller import FileController
import PySide2.QtCore


class GuiHelper:

    @staticmethod
    def populate_list_with_track_info(track: MKVTrack, list_widget: QListWidget):
        """
        Populate the listwidget with the selected track's information
        :param self:
        :param track:
        :param list_widget:
        :return:
        """

        track_name = "N/A"
        if track.track_name is not None:
            track_name = track.track_name

        list_widget.clear()
        list_widget.addItem(" File Path: " + track.file_path)
        list_widget.addItem(" Track ID: " + str(track.track_id))
        list_widget.addItem(" Track Name: " + track_name)
        list_widget.addItem(" Track Type: " + track._track_type)
        list_widget.addItem(" Track Codec: " + track._track_codec)
        list_widget.addItem(" Language: " + track.language)
        list_widget.addItem(" Default Track: " + str(track.default_track))
        list_widget.addItem(" Forced Track: " + str(track.forced_track))

    @staticmethod
    def gather_all_selected_track(list_widget: QListWidget, file_controller: FileController):

        user_selected_track = []
        for index in range(list_widget.count()):

            item = list_widget.item(index)
            if item.checkState() == PySide2.QtCore.Qt.Checked:
                user_selected_track.append(file_controller.get_track(index))

        return user_selected_track
