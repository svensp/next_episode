from next_episode import show_nfo
from .lib import expected_file, mocked_handle, assert_file_written
import mock


class TestFileGenerateShowNfo:

    @mock.patch('next_episode.show_nfo.open', create=True)
    @mock.patch('next_episode.show_nfo.uuid')
    @mock.patch('next_episode.show_nfo.os')
    def test_should_create_tvshow_nfo_file(self, mock_os, uuid, mock_open):
        mock_directory(mock_os)
        uuid.uuid4.return_value = 'mock-uuid'

        nfo = show_nfo.ShowNfo.fromDirectory('.')
        nfo.save()

        assert_file_written(mock_open, '/opt/TV Series/tvshow.nfo', expected_file('tvshow.nfo', {
            'UUID': 'mock-uuid',
            'TITLE': 'TV Series'
        }))

    @mock.patch('next_episode.show_nfo.open', create=True)
    @mock.patch('next_episode.show_nfo.os')
    def test_should_not_generate_nfo_if_it_already_exists(self, mock_os, mock_open):
        mock_os.path.exists.return_value = True

        nfo = show_nfo.ShowNfo.fromDirectory('.')
        nfo.save()

        assert not mock_open.called

def mock_directory(mock_os):
    mock_os.sep = '/'
    mock_os.path.exists.return_value = False
    mock_os.path.abspath.return_value = '/opt/TV Series'
