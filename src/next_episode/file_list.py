import re
import os

class NotFoundException(Exception):
    pass

class File:
    def __init__(self, name):
        self.directoryPath = None
        self.name = name
        self.match = re.match('.+\.s([0-9]+)e([0-9]+)\..+', name)

    @staticmethod
    def fromRelativePath(relativePath):
        file = File.fromName( os.path.basename(relativePath) )

        target = os.path.abspath(relativePath)
        file.directoryPath = os.path.dirname(target)

        return file

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

    def siblings(self):
        return list( filter( lambda file: file != self.name, os.listdir(self.directoryPath) ) )

    def applyNextEpisodeTag(self):
        self.applyTag(self.nextEpisodeTag() )

    def applyNextSeasonTag(self):
        self.applyTag(self.nextSeasonTag() )

    def applyTag(self, tag):
        if self.hasTag():
            return

        os.rename(
            self.directoryPath+'/'+self.name,
            self.directoryPath+'/'+self.nameWithTag(tag)
                  )

    def nameWithTag(self, tag):
        name, _, extension = self.nameTagExtension()
        return '.'.join([name, tag, extension])

    def nextEpisodeTag(self):
        fileList = FileList.fromFilenames( self.siblings() )

        return "s%02de%02d" % (fileList.currentSeason(), fileList.nextEpisode())

    def nextSeasonTag(self):
        fileList = FileList.fromFilenames( self.siblings() )

        return "s%02de%02d" % (fileList.nextSeason(), 1)

    def nameTagExtension(self):
        match = re.match('(.*?)(\.s[0-9]+e[0-9]+)?\.([^.]+)', self.name)
        return [match.group(1), match.group(2), match.group(3)]

    def hasTag(self):
        _, tag, _ = self.nameTagExtension()
        return tag is not None


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
