import sys
import logging
import PySide2.QtGui
from PySide2.QtWidgets import QApplication, QMainWindow, QFileDialog, QListWidgetItem
from ui_home import Ui_MainWindow
from file_controller import FileController
from pymkv_wrapper import PymkvWrapper
from gui_helper import GuiHelper
from output_wrapper import OutputWrapper

import threading

logger = logging.getLogger()


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        sys.stdout = OutputWrapper(self.ui.log)
        sys.stderr = OutputWrapper(self.ui.log)
        sys.stdin = OutputWrapper(self.ui.log)

        self.connect_single_buttons()
        self.connect_batch_buttons()

        self.single_file_processor = FileController()
        self.connect_signal()

    def connect_single_buttons(self):
        self.ui.button_single_add_file.clicked.connect(self.add_track_to_single_list)
        self.ui.button_single_browse_dir.clicked.connect(self.set_single_output_directory)
        self.ui.button_sinlge_mux.clicked.connect(self.mux_single_file)

    def connect_batch_buttons(self):
        self.ui.button_batch_select_input1.clicked.connect(None)

    def add_track_to_single_list(self):
        file_name = FileController.open_dialog_for_file()[0]
        track_list = PymkvWrapper.process_file(file_name)
        self.single_file_processor.generate_item(track_list=track_list, list_widget=self.ui.list_single_avaltrack)

    def connect_signal(self):
        self.ui.list_single_avaltrack.currentItemChanged.connect(self.populate_track_info)

    def set_single_output_directory(self):
        self.ui.lineedit_single_ouputdir.setText(FileController.open_dialog_for_directory_name())

    def populate_track_info(self):
        track = self.single_file_processor.get_track(self.ui.list_single_avaltrack.currentRow())
        GuiHelper.populate_list_with_track_info(track, self.ui.list_single_trackinfo)

    def mux_single_file(self):
        _single_user_selected_tracks = GuiHelper.gather_all_selected_track(self.ui.list_single_avaltrack,
                                                                           self.single_file_processor)

        output_dir = self.ui.lineedit_single_ouputdir.text() + "/"
        output_name = self.ui.lineedit_single_outputname.text()

        mux_thread = threading.Thread(target=PymkvWrapper.generate_file_from_tracks, args=(_single_user_selected_tracks, output_dir,
                                      output_name))
        mux_thread.start()


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
