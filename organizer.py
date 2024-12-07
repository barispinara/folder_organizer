import os
import shutil
import json
import re

EXTENSION_FILE_NAME = "extensions.json"


class Organizer:

    def __init__(self, given_path: str):
        self.path = self._return_path_if_exists(input_path=given_path)
        self._extension_list = self._read_extension_json_file()

    def _return_path_if_exists(self, input_path: str) -> str:
        if os.path.exists(input_path):
            return input_path
        raise NotADirectoryError(f"The given path '{input_path}' does not exist")

    def _read_extension_json_file(self) -> dict:
        with open(EXTENSION_FILE_NAME, "r") as file:
            extension_dict = json.load(file)
        return extension_dict

    def _list_path_dir(self, path: str, dict_of_file_name_and_path: dict = {}):
        list_of_directories = os.scandir(path)
        for x in list_of_directories:
            if x.is_dir():
                self._list_path_dir(
                    path=x.path, dict_of_file_name_and_path=dict_of_file_name_and_path
                )
                continue
            dict_of_file_name_and_path[x.name] = x.path

        return dict_of_file_name_and_path

    def _move_file(self, file_path: str, destination: str):
        if not self._is_paths_equal(curr_path=file_path,
                                destination_path=destination):
            shutil.move(file_path, destination)

    def _is_paths_equal(self, curr_path: str, destination_path: str) -> bool:
        curr_path_normalized = os.path.normpath(curr_path)
        destination_path_normalized = os.path.normpath(destination_path)

        curr_path_normalized = (
            os.path.dirname(curr_path_normalized)
            if os.path.isfile(curr_path_normalized)
            else curr_path_normalized
        )
        destination_path_normalized = (
            os.path.dirname(destination_path_normalized)
            if os.path.isfile(destination_path_normalized)
            else destination_path_normalized
        )
        
        return curr_path_normalized == destination_path_normalized

    def _create_folder_if_does_not_exist(self, folder_name: str):
        new_path = f"{self.path}/{folder_name}"
        if not os.path.exists(new_path):
            os.makedirs(new_path)

    def _get_extension_name_of_given_file_name(self, file_name: str) -> str:
        return f".{file_name.split(".")[-1]}"

    def _get_file_name_from_full_path(self, file_path: str) -> str:
        return f".{re.split(r"[\\/]", file_path)[-1]}"

    def start_organize_files(self):
        dict_of_files = self._list_path_dir(self.path)
        for key, value in dict_of_files.items():
            curr_extension_name = self._get_extension_name_of_given_file_name(
                file_name=key
            )
            target_folder_name = self._extension_list.get(curr_extension_name, "Other")
            self._create_folder_if_does_not_exist(folder_name=target_folder_name)
            self._move_file(
                file_path=value, destination=f"{self.path}/{target_folder_name}"
            )
