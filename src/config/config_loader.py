import json


class ConfigLoader:
    @staticmethod
    def load_config(file_path):
        with open(file_path, "r", encoding="utf-8") as file:
            return json.load(file)
