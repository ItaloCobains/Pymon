import pathlib
import os

from os import listdir
from os.path import isfile, join
from pathlib import Path


def getAllFilesInRepo() -> list:
    dir = pathlib.Path(os.path.dirname(os.path.realpath(__file__)))
    dir = str(dir).replace('sample', '')
    onlyfiles = [f for f in listdir(dir) if isfile(join(dir, f))]
    return onlyfiles

def returnSizeOfArrayFiles(files: list):
    data: list = []
    for file in files:
        data.append(returnSizeOfFile(file))
    return data


def returnSizeOfFile(file: str) -> int:
    size = Path(file).stat().st_size
    return size

def findSettingsFile() -> bool:
    dir = pathlib.Path(os.path.dirname(os.path.realpath(__file__)))
    file = dir.glob('settings.pyic')
    if file:
        return True
    return False

def readSettingsFile() -> str:
    f = open('settings.pyic', 'r')
    data = f.readline()
    data = filterData(data)
    return data


def filterData(data: str) -> str:
    data = data.replace("command=", "")
    data = data.replace("'", "")
    return data

def verifyFileChange(fileInitial: list, fileNew: list) -> bool:
    if fileInitial == fileNew:
        return False
    return True

