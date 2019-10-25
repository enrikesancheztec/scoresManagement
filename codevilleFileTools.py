from pathlib import Path


class FileValidator:
    @staticmethod
    def validateFileExists(filenameAndPath):
        file = Path(filenameAndPath)
        return file.is_file()


class FileReader:
    @staticmethod
    def readScoresFile(filenameAndPath):
        file = open(filenameAndPath, "r")

        readList = []

        for line in file:
            fields = line.strip('\n').split(",")
            if len(fields) == 2:
                competitor = Competitor(fields[0], fields[1])
                readList.append(competitor)
            else:
                return None

        return readList


class Competitor:
    fullname = ""
    score = 0

    def __init__(self, fullname, score):
        self.fullname = fullname
        self.score = score

    def __str__(self):
        return self.fullname + " " + self.score
