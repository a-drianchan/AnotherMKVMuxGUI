import logging

import pymkv.MKVTrack as mkvtrack
import pymkv.MKVFile as mkvfile
import pymkv.MKVAttachment as mkvattachment

logger = logging.getLogger(__name__)


class PymkvWrapper:

    @staticmethod
    def process_file(file_path : str):
        mkv_file = mkvfile(file_path)
        track_list = mkv_file.get_track()
        return track_list

    @staticmethod
    def get_all_track_information(mkv_file: mkvfile):
        track_list = mkv_file.get_track()
        return track_list

    @staticmethod
    def open_mkv_file(path: str):
        mkv_file = mkvfile(path)
        return mkv_file

    @staticmethod
    def generate_file_from_tracks(track_list: mkvtrack, output_dir: str, output_name: str):
        mkv = mkvfile()
        for track in track_list:
            mkv.add_track(track)

        if output_name[-4:] != ".mkv":
            output_name = output_name + ".mkv"

        mkv.mux(output_dir + output_name)
