from PySide2.QtWidgets import QFileDialog, QListWidgetItem, QListWidget
import logging
import glob

logger = logging.getLogger(__name__)


class FileDialogHelper:

    @staticmethod
    def open_dialog_for_file():
        """
            Function wrapper to open file dialogs for selecting mkv files
        :return: a list of selected files
        """
        file_names = None

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
    def open_dialog_for_directory(mode: str):
        """
            Function wrapper to open file dialogs for selecting mkv files
        :return: a list of selected files
        """
        if mode == "single":
            extensions = ["/*.mkv", "/*.ass", "/*.srt", "/*.flac", "/*.ac3"]
        elif mode == "batch":
            extensions = ["/*.mkv"]
        else:
            logger.error("Invalid mode")
            return None

        file_list = []

        dialog = QFileDialog()
        dialog.setFileMode(QFileDialog.DirectoryOnly)
        if dialog.exec_():
            directory_name = dialog.selectedFiles()
            logger.debug(directory_name)
            for extension in extensions:
                logger.debug("Searching inside " + directory_name[0] + extension)
                file_list.extend(glob.glob(directory_name[0] + extension))

            for file in file_list:
                logger.info(file + " found")

            logger.info(str(len(file_list)) + " files found.")
            return file_list

    @staticmethod
    def open_dialog_for_directory_name():
        """
            Function wrapper to open file dialogs and return name of the path
        :return: a list of selected files
        """
        dialog = QFileDialog()
        dialog.setFileMode(QFileDialog.DirectoryOnly)
        if dialog.exec_():
            directory_name = dialog.selectedFiles()
            return directory_name[0]

