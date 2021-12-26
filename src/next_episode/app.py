#!/sbin/python3

import sys

from .file_list import FileList, File

class App:
    def nextEpisode(self):
        self.assertFileArgumentPassed()

        target = File.fromRelativePath(sys.argv[1])
        target.applyNextEpisodeTag()
        return 0

    def nextSeason(self):
        self.assertFileArgumentPassed()

        target = File.fromRelativePath(sys.argv[1])
        target.applyNextSeasonTag()
        return 0

    def assertFileArgumentPassed(self):
        if len(sys.argv) < 2:
            self.printHelp()
            sys.exit(1)

    def printHelp(self):
        print("USAGE")
        print(sys.argv[0]+" path/to/next/file")
