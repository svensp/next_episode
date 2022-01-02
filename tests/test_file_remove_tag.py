from next_episode import file_list
from .lib import mock_current_directory
import mock

class TestFileRemoveTag:

    @mock.patch('next_episode.file_list.os')
    def test_should_remove_s01e01_tag(self, mock_os):
        mock_current_directory(mock_os, [], 'test.s01e01.txt')
        file = file_list.File.fromRelativePath('./test.s01e01.txt')

        file.removeTag()
        mock_os.rename.assert_called_with('./test.s01e01.txt', './test.txt')

    @mock.patch('next_episode.file_list.os')
    def test_should_remove_s01e01_tag_from_artwork_if_preset(self, mock_os):
        mock_current_directory(mock_os, ['test.s01e01-thumb.jpg'], 'test.s01e01.txt')
        file = file_list.File.fromRelativePath('./test.s01e01.txt')

        file.removeTag()
        mock_os.rename.assert_called_with('./test.s01e01-thumb.jpg', './test.jpg')

