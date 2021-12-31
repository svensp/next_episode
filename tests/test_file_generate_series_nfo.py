from next_episode import series_nfo
from .lib import expected_file, mocked_handle, assert_file_written
import mock


class TestFileGenerateSeriesNfo:

    @mock.patch('next_episode.series_nfo.open', create=True)
    @mock.patch('next_episode.series_nfo.uuid')
    @mock.patch('next_episode.series_nfo.os')
    def test_should_create_tvseries_nfo_file(self, mock_os, uuid, mock_open):
        mock_directory(mock_os)
        uuid.uuid4.return_value = 'mock-uuid'

        nfo = series_nfo.SeriesNfo.fromDirectory('.')
        nfo.save()

        assert_file_written(mock_open, '/opt/TV Series/tvseries.nfo', expected_file('tvseries.nfo', {
            'UUID': 'mock-uuid',
            'TITLE': 'TV Series'
        }))

    @mock.patch('next_episode.series_nfo.open', create=True)
    @mock.patch('next_episode.series_nfo.os')
    def test_should_not_generate_nfo_if_it_already_exists(self, mock_os, mock_open):
        mock_os.path.exists.return_value = True

        nfo = series_nfo.SeriesNfo.fromDirectory('.')
        nfo.save()

        assert not mock_open.called

    @mock.patch('next_episode.series_nfo.open', create=True)
    @mock.patch('next_episode.series_nfo.uuid')
    @mock.patch('next_episode.series_nfo.os')
    def test_should_create_tvseries_nfo_file(self, mock_os, uuid, mock_open):
        mock_directory(mock_os)
        uuid.uuid4.return_value = 'mock-uuid'
        mock_os.listdir.return_value = ['TV Series.jpg']

        nfo = series_nfo.SeriesNfo.fromDirectory('.')
        nfo.save()

        assert_file_written(mock_open, '/opt/TV Series/tvseries.nfo', expected_file('tvseries-withartwork.nfo', {
            'UUID': 'mock-uuid',
            'TITLE': 'TV Series',
            'ARTWORK': 'TV Series.jpg'
        }))

def mock_directory(mock_os):
    mock_os.sep = '/'
    mock_os.path.exists.return_value = False
    mock_os.path.abspath.return_value = '/opt/TV Series'
