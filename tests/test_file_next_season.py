from next_episode import file_list
from .lib import mock_current_directory
import mock


class TestFileApplyNextSeasonTag:

    @mock.patch('next_episode.file_list.os')
    def test_should_add_s01e01_tag_if_none_is_present(self, mock_os):
        mock_current_directory(mock_os, [])
        file = file_list.File.fromRelativePath('./test.txt')

        file.applyNextSeasonTag()
        mock_os.rename.assert_called_with('./test.txt', './test.s01e01.txt')

    @mock.patch('next_episode.file_list.os')
    def test_should_add_next_tag_if_none_is_present(self, mock_os):
        mock_current_directory(mock_os, [
            'oink.s01e03.mp4',
            'oink.s02e02.mp4',
        ])

        file = file_list.File.fromRelativePath('./test.txt')

        file.applyNextSeasonTag()
        mock_os.rename.assert_called_with('./test.txt', './test.s03e01.txt')

    @mock.patch('next_episode.file_list.os')
    def test_should_do_nothing_if_tag_is_absent(self, mock_os):
        mock_current_directory(mock_os, [], 'test.txt')

        file = file_list.File.fromRelativePath('./test.txt')

        file.removeTag()
        assert not mock_os.rename.called

    @mock.patch('next_episode.file_list.os')
    def test_should_rename_file_to_same_name_without_tag(self, mock_os):
        mock_current_directory(mock_os, [], 'test.s02e01.txt')

        file = file_list.File.fromRelativePath('./test.s02e01.txt')

        file.removeTag()
        mock_os.rename.assert_called_with('./test.s02e01.txt', './test.txt')

