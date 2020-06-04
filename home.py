import sys
import logging
import threading
from events import Events

import PySide2.QtGui
from PySide2.QtWidgets import QApplication, QMainWindow, QFileDialog, QListWidgetItem

from ui_home import Ui_MainWindow
from file_controller import FileController
from batch_file_controller import BatchFileController
from pymkv_wrapper import PymkvWrapper
from gui_helper import GuiHelper
from output_wrapper import OutputWrapper
from file_dialog_helper import FileDialogHelper


logger = logging.getLogger()


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):

        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.events = Events()

        sys.stdout = OutputWrapper(self.ui.log)
        sys.stderr = OutputWrapper(self.ui.log)
        sys.stdin = OutputWrapper(self.ui.log)

        self.single_file_controller = FileController()
        self.batch_file_controller = BatchFileController()

        self.connect_single_buttons()
        self.connect_batch_buttons()
        self.connect_callback_functions()

        self.connect_auto_update()

    """
    Functions to connect GUI to the proper functions
    """

    def connect_single_buttons(self):
        """
        Connect the button clicked signals to the corresponding functions for the single file mux
        :return: None
        """

        self.ui.button_single_add_file.clicked.connect(self.add_track_to_single_list)
        self.ui.button_single_clear.clicked.connect(self.clear_track)
        self.ui.button_single_browse_dir.clicked.connect(self.set_single_output_directory)
        self.ui.button_sinlge_mux.clicked.connect(self.mux_single_file)

    def connect_batch_buttons(self):
        """
        Connect the button clicked signals to the corresponding functions for the batch file mux
        :return: None
        """
        self.ui.button_batch_select_input1.clicked.connect(lambda: self.get_file_from_directory(1))
        self.ui.button_batch_select_input2.clicked.connect(lambda: self.get_file_from_directory(2))
        self.ui.button_batch_mux.clicked.connect(self.batch_mux)
        self.ui.button_batch_clear.clicked.connect(self.batch_file_controller.clear_all)
        self.ui.button_batch_select_output.clicked.connect(self.get_output_directory_name)

    def connect_auto_update(self):
        self.ui.list_batch_reference_1.itemChanged.connect(
            lambda: self.batch_file_controller.gather_all_selected_track(self.ui.list_batch_reference_1, self.ui.list_batch_reference_2))
        self.ui.list_batch_reference_2.itemChanged.connect(
            lambda: self.batch_file_controller.gather_all_selected_track(self.ui.list_batch_reference_1, self.ui.list_batch_reference_2))

    def connect_callback_functions(self):
        """
        Connecting non-button press signals to the correct slots
        :return:
        """
        self.single_file_controller.events.on_clear += self.callback_clear_track
        self.single_file_controller.events.single_track_item_generated += self.ui.list_single_avaltrack.addItem

        self.ui.list_single_avaltrack.currentItemChanged.connect(self.populate_track_info)
        self.batch_file_controller.events.batch_file_item_generated += self.update_batch_list
        self.batch_file_controller.events.batch_item_generated += self.update_batch_list

        self.batch_file_controller.events.ref_tracks_generated += self.update_reference_list
        self.batch_file_controller.events.clear_all += self.clear_batch_mode




    """
    Functions that link the single fix mux portion to the PySide2 GUI  
    """

    def clear_track(self):
        """
        Clear loaded track list in the single file mux mode.
        :return:
        """
        self.single_file_controller.clear_track_list()

    def callback_clear_track(self):
        """
        Method to run when receiving a signal from the singe file processor
        :return:
        """
        self.ui.list_single_avaltrack.clear()
        self.ui.list_single_trackinfo.clear()

    def add_track_to_single_list(self):
        """
        Add the selected tracks selected from QFileDialog to the single file processor
        :return:
        """
        file_name = FileDialogHelper.open_dialog_for_file()[0]
        track_list = PymkvWrapper.process_file(file_name)
        self.single_file_controller.generate_item(track_list=track_list)

    def set_single_output_directory(self):
        """
        Set the output directory for the single file mux mode
        :return:
        """
        self.ui.lineedit_single_ouputdir.setText(FileDialogHelper.open_dialog_for_directory_name())


    def populate_track_info(self):
        """
        Populate the track information in the single file mux with the selected track
        :return:
        """
        if len(self.single_file_controller.single_track_list) > 0:
            track = self.single_file_controller.get_track(self.ui.list_single_avaltrack.currentRow())
            GuiHelper.populate_list_with_track_info(track, self.ui.list_single_trackinfo)
        else:
            self.ui.list_single_trackinfo.clear()

    def mux_single_file(self):
        """
        Start a thread to mux the selected tracks together for muxing single files
        :return:
        """
        _single_user_selected_tracks = GuiHelper.gather_all_selected_track(self.ui.list_single_avaltrack,
                                                                           self.single_file_controller)

        output_dir = self.ui.lineedit_single_ouputdir.text() + "/"
        output_name = self.ui.lineedit_single_outputname.text()

        mux_thread = threading.Thread(target=PymkvWrapper.generate_file_from_tracks, args=(_single_user_selected_tracks, output_dir,
                                      output_name))
        mux_thread.start()

    """
    Methods for use in the batch mux mode.
    """
    def get_file_from_directory(self, source: int):
        if source == 1:
            self.batch_file_controller.source_1_list = FileDialogHelper.open_dialog_for_directory(mode="batch")

        elif source == 2:
            self.batch_file_controller.source_2_list = FileDialogHelper.open_dialog_for_directory(mode="batch")

    def get_output_directory_name(self):
            self.batch_file_controller.output_directory = FileDialogHelper.open_dialog_for_directory_name()
            self.ui.label_batch_output_dir_name.setText(self.batch_file_controller.output_directory)

    def update_batch_list(self, list_item: QListWidgetItem, list_num: str):
        """
        Add item to the file list
        :param list_item:
        :param list_num:
        :return:
        """
        if list_num == 1:
            self.ui.list_batch_source1.addItem(list_item)
            self.ui.label_batch_file_count_1.setText("File Count: " + str(len(self.batch_file_controller.source_1_list)))
            if self.ui.list_batch_source1.count() == 1:
                self.batch_file_controller.generate_track_item(1)
        elif list_num == 2:
            self.ui.list_batch_source2.addItem(list_item)
            self.ui.label_batch_file_count_2.setText("File Count: " + str(len(self.batch_file_controller.source_2_list)))
            if self.ui.list_batch_source2.count() == 1:
                self.batch_file_controller.generate_track_item(2)

    def update_reference_list(self, file_name, track_item, list_num: int):
        """
        Add in track information using the first item in the source list
        :param track_item:
        :param list_num:
        :return:
        """
        if list_num == 1:
            self.ui.label_batch_ref_1.setText(file_name)
            self.ui.list_batch_reference_1.addItem(track_item)
        elif list_num == 2:
            self.ui.label_batch_ref_2.setText(file_name)
            self.ui.list_batch_reference_2.addItem(track_item)

    def batch_mux(self):
        batch_mux = threading.Thread(target=self.batch_file_controller.batch_mux_files)
        batch_mux.start()

    def clear_batch_mode(self):
        self.ui.list_batch_reference_1.clear()
        self.ui.list_batch_reference_2.clear()

        self.ui.list_batch_source1.clear()
        self.ui.list_batch_source2.clear()

        self.ui.label_batch_ref_1.setText("No file loaded")
        self.ui.label_batch_ref_1.setText("No file loaded"
                                          "")
        self.ui.label_batch_file_count_1.setText("File Count: 0")
        self.ui.label_batch_file_count_2.setText("File Count: 0")


if __name__ == "__main__":

    # Configure logger settings
    logger.setLevel(logging.DEBUG)
    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    ch.setFormatter(formatter)
    logger.addHandler(ch)

    # Initiate the GUI
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()
    logger.debug("GUI opened")
    sys.exit(app.exec_())
