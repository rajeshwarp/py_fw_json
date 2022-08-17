# Read json file and return the data in python dictionary format
import json
from types import SimpleNamespace


class ReadJson():
    def __init__(self, fileName):
        self.fileName = fileName

    def readJson(self):
        with open(self.fileName) as json_file:
            data = json.load(json_file,object_hook=lambda d: SimpleNamespace(**d))
            return data

    def readJsonByKey(self, key):
        with open(self.fileName) as json_file:
            data = json.load(json_file)
            return data[key]

    def readJsonByKeyAndValue(self, key, value):
        with open(self.fileName) as json_file:
            data = json.load(json_file)
            return data[key][value]


