from next_episode.artwork import Artwork
from .lib import mock_current_directory
import mock

class TestFileFillTag:

    @mock.patch('next_episode.artwork.shutil')
    @mock.patch('next_episode.artwork.os')
    def test_should_rename_to_banner_if_not_present(self, mock_os, mock_shutil):
        mock_current_directory(mock_os, [], 'test.jpg')
        file = Artwork('./test.jpg')

        file.as_next_season()
        mock_shutil.copy.assert_called_with('./test.jpg', './banner.jpg')

    @mock.patch('next_episode.artwork.shutil')
    @mock.patch('next_episode.artwork.os')
    def test_should_rename_to_season_01_if_banner_is_present(self, mock_os, mock_shutil):
        mock_current_directory(mock_os, [
            'banner.jpg'
        ], 'test.jpg')
        file = Artwork('./test.jpg')

        file.as_next_season()
        mock_shutil.copy.assert_called_with('./test.jpg', './season01-banner.jpg')

    @mock.patch('next_episode.artwork.shutil')
    @mock.patch('next_episode.artwork.os')
    def test_should_rename_to_season_plus_one_if_all_before_are_present(self, mock_os, mock_shutil):
        mock_current_directory(mock_os, [
            'banner.jpg',
            'season01-banner.jpg',
            'season02-banner.jpg',
            'season03-banner.jpg',
        ], 'test.jpg')
        file = Artwork('./test.jpg')

        file.as_next_season()
        mock_shutil.copy.assert_called_with('./test.jpg', './season04-banner.jpg')
