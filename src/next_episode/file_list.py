import re

class NotFoundException(Exception):
    pass

class File:
    def __init__(self, name):
        self.match = re.match('.+\.s([0-9]+)e([0-9]+)\..+', name)

    @staticmethod
    def fromName(name):
        return File(name)

    def appendSeasonList(self, files):
        if self.match:
            files.append(self)

    def season(self):
        return int( self.match.group(1) )

    def episode(self):
        return int( self.match.group(2) )

class FileList:
    def __init__(self, fileNames):
        self.fileNames = fileNames

    @staticmethod
    def fromFilenames(fileNames):
        return FileList(fileNames)

    def nextSeason(self):
        try:
            return self.highestSeason() + 1
        except NotFoundException:
            return 1

    def currentSeason(self):
        try:
            return self.highestSeason()
        except NotFoundException:
            return 1

    def currentEpisode(self):
        try:
            return self.highestEpisode()
        except NotFoundException:
            return 0

    def nextEpisode(self):
        try:
            return self.highestEpisode() + 1
        except NotFoundException:
            return 1

    def highestSeason(self):
        return self.highestIn(self.filesFromFileNames(), lambda file: file.season())

    def highestEpisode(self):
        highestSeason = self.highestIn(self.filesFromFileNames(), lambda file: file.season())
        episodesInSeason = self.episodesInSeason(highestSeason)
        return self.highestIn(episodesInSeason, lambda file: file.episode())

    def episodesInSeason(self, seasonNumber):
        return list( filter(lambda file: file.season() == seasonNumber, self.filesFromFileNames()) )

    def highestIn(self, files, fileAttribute):
        if len(files) == 0:
            raise NotFoundException

        highest = 1
        for file in files:
            if fileAttribute(file) > highest:
                highest = fileAttribute(file)
        return highest

    def filesFromFileNames(self):
        files = []

        for fileName in self.fileNames:
            file = File.fromName(fileName)
            file.appendSeasonList(files)

        return files
