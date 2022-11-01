import os

from . import helpers
from colorama import Fore

class Pymon:
    def __init__(self: object) -> None:
        self.files = helpers.getAllFilesInRepo()
        self.sizeData = helpers.returnSizeOfArrayFiles(self.files)
        self.command = helpers.readSettingsFile()

    def __iter__(self: object) -> object:
        return self


    def main(self: object) -> None:
        while(True):
            print(Fore.GREEN, "Executing file")
            print(Fore.WHITE, '\n')
            os.system(self.command)
            while(True):
                data = helpers.returnSizeOfArrayFiles(self.files)
                result: bool = helpers.verifyFileChange(self.sizeData, data)
                self.sizeData = data
                if result:
                    print('file changed')
                    break
            os.system("clear")
            os.system("^C")
            os.system("clear")

