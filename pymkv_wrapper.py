import logging

import pymkv.MKVTrack as MKVtrack
import pymkv.MKVFile as MKVfile
import pymkv.MKVAttachment as mkvattachment

logger = logging.getLogger(__name__)


class PymkvWrapper:

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
