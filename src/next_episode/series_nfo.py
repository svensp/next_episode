import os
import uuid

class SeriesNfo:
    @staticmethod
    def fromDirectory(directory):
        return SeriesNfo(directory)

    def __init__(self, directory):
        self.directory = os.path.abspath(directory)

    def save(self):
        if os.path.exists(self.tv_series_nfo()):
            return

        with open(self.tv_series_nfo(), 'w') as file:
            file.write(
                '<?xml version="1.0" encoding="UTF-8" standalone="yes" ?>\n'
                '<tvshow>\n'
                '    <title>' + self.title_from_directory() + '</title>\n'
                '    <uniqueid type="home" default="true">' + str(uuid.uuid4()) + '</uniqueid>\n'
                '</tvshow>'
            )

    def tv_series_nfo(self):
        return self.directory+'/tvseries.nfo'

    def title_from_directory(self):
        parts = self.directory.split(os.sep)
        return last(parts)


def last(_list):
    return _list[len(_list) - 1]