import logging

import pymkv.MKVTrack as MKVtrack
import pymkv.MKVFile as MKVfile
import pymkv.MKVAttachment as mkvattachment

logger = logging.getLogger(__name__)


class PymkvWrapper(object):

    @staticmethod
    def process_file(file_path : str):
        mkv_file = MKVfile(file_path)
        track_list = mkv_file.get_track()
        return track_list

    @staticmethod
    def get_all_track_information(mkv_file: MKVfile):
        track_list = mkv_file.get_track()
        return track_list

    @staticmethod
    def open_mkv_file(path: str):
        mkv_file = MKVfile(path)
        return mkv_file

    @staticmethod
    def generate_file_from_tracks(track_list: MKVtrack, output_dir: str, output_name: str):
        mkv = MKVfile()
        for track in track_list:
            mkv.add_track(track)

        if output_name[-4:] != ".mkv":
            output_name = output_name + ".mkv"

        mkv.mux(output_dir + output_name)

    @staticmethod
    def batch_mux_files(mkv_list_1, mkv_list_2, settings_1, settings_2, output_directory, output_name):

        if len(mkv_list_1) == len(mkv_list_2):

            for item_num in range(0, len(mkv_list_1)):
                mkv = MKVfile()
                # Add tracks from source 1
                mkv_file_1 = MKVfile(mkv_list_1[item_num])
                track_list_1 = mkv_file_1.get_track()

                for track_number in settings_1:
                    mkv.add_track(track_list_1[track_number])

                mkv_file_2 = MKVfile(mkv_list_2[item_num])
                track_list_2 = mkv_file_2.get_track()
                for track_number in settings_2:
                    mkv.add_track(track_list_2[track_number])

                # Add tracks from source 2
                if output_name[-4:] != ".mkv":
                    output_name = output_name + ".mkv"

                output_name = str(item_num) + ".mkv"
                logger.debug("Output directory is: " + output_directory + "/" +  output_name)
                mkv.mux(output_directory + "/" +  output_name)

        else:
            logger.error("Source 1 and Source 2 directory have different numbers of files. Unable to batch mux.")
            pass
