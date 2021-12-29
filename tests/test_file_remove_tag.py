from next_episode import file_list
from .lib import mock_current_directory
import mock

class TestFileRemoveTag:

    @mock.patch('next_episode.file_list.os')
    def test_should_add_s01e01_tag_if_none_is_present(self, mock_os):
        mock_current_directory(mock_os, [])
        file = file_list.File.fromRelativePath('./test.txt')

        file.applyNextSeasonTag()
        mock_os.rename.assert_called_with('./test.txt', './test.s01e01.txt')

