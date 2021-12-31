class ArtworkFactory:
    @staticmethod
    def from_path(path):
        return Artwork(path)


class Artwork:
    def __init__(self, path):
        self.path = path

    def thumb(self):
        return '<thumb preview="">'+self.path+'</thumb>\n'


