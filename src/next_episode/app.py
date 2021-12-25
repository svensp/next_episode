#!/sbin/python3

import sys
import os
import re

class App:
    def nextEpisode(self):
        self.assertFileArgumentPassed();

        target = os.path.abspath(sys.argv[1])
        targetDirectory = os.path.dirname(target);
        files = os.listdir(targetDirectory)
        seasonNumber = self.findCurrentSeason(files)
        print("Current season: "+str(seasonNumber))
        return 0

    def assertFileArgumentPassed(self):
        if len(sys.argv) < 2:
            print("USAGE")
            print(sys.argv[0]+" path/to/next/file")
            sys.exit(1)

    def parseFilenames(self, files):
        seasonNumber = 1

        pattern = re.compile('/.+\.s([0-9]+)e([0-9]+)\..+/')
        for file in files:
            match = pattern.match(file)
            if match:
                newSeason = match.group(1)

        return seasonNumber