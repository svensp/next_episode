from next_episode import file_list
from .lib import mock_current_directory, expected_file, assert_file_written
import mock


class TestFileGenerateNfo:

    @mock.patch('next_episode.file_list.open', create=True)
    @mock.patch('next_episode.file_list.uuid')
    @mock.patch('next_episode.file_list.os')
    def test_should_create_nfo_file(self, mock_os, uuid, mock_open):
        mock_current_directory(mock_os, [], 'test.s01e01.txt')
        uuid.uuid4.return_value = 'mock-uuid'

        file = file_list.File.fromRelativePath('./test.s01e01.txt')
        file.generate_nfo()

        assert_file_written(mock_open, './test.s01e01.nfo', expected_file('test.s01e01.nfo', {'UUID': 'mock-uuid'}))

    @mock.patch('next_episode.file_list.open', create=True)
    @mock.patch('next_episode.file_list.os')
    def test_should_not_generate_nfo_if_tag_is_missing(self, mock_os, mock_open):
        mock_current_directory(mock_os, [], 'test.txt')

        file = file_list.File.fromRelativePath('./test.txt')
        file.generate_nfo()

        assert not mock_open.called
