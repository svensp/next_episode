from next_episode import file_list
from .lib import mock_current_directory
import mock

class TestFileFillTag:

    @mock.patch('next_episode.file_list.os')
    def test_should_add_first_missing_tag(self, mock_os):
        mock_current_directory(mock_os, [
            'episode.s01e01.mp4',
            'episode.s01e02.mp4',
            'episode.s01e03.mp4',
            'episode.s02e02.mp4',
            'episode.s02e03.mp4',
            'episode.s03e01.mp4',
            'episode.s03e02.mp4',
            'episode.s03e03.mp4',
        ])
        file = file_list.File.fromRelativePath('./test.txt')

        file.applyFillerTag()
        mock_os.rename.assert_called_with('./test.txt', './test.s02e01.txt')

    @mock.patch('next_episode.file_list.os')
    def test_should_add_next_episode_if_none_is_missing(self, mock_os):
        mock_current_directory(mock_os, [
            'episode.s01e01.mp4',
            'episode.s01e02.mp4',
            'episode.s01e03.mp4',
        ])
        file = file_list.File.fromRelativePath('./test.txt')

        file.applyFillerTag()
        mock_os.rename.assert_called_with('./test.txt', './test.s01e04.txt')

    @mock.patch('next_episode.file_list.os')
    def test_should_add_missing_tag_in_last_season(self, mock_os):
        mock_current_directory(mock_os, [
            'episode.s01e02.mp4',
            'episode.s01e03.mp4',
        ])
        file = file_list.File.fromRelativePath('./test.txt')

        file.applyFillerTag()
        mock_os.rename.assert_called_with('./test.txt', './test.s01e01.txt')
