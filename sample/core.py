from . import helpers
import os
import time

class Pymon:
    def __init__(self) -> None:
        self.files = helpers.getAllFilesInRepo()
        self.sizeData = helpers.returnSizeOfArrayFiles(self.files)
        self.command = helpers.readSettingsFile()

    def __iter__(self: object) -> object:
        return self


    def main(self) -> None:
        while(True):
            os.system(self.command)
            print("Executing command")
            while(True):
                data = helpers.returnSizeOfArrayFiles(self.files)
                result: bool = helpers.verifyFileChange(self.sizeData, data)
                self.sizeData = data
                if result:
                    break
            os.system("^C")

