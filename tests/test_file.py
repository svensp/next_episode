from next_episode import file_list
import mock


class TestFileApplyNextEpisodeTag:

    @mock.patch('next_episode.file_list.os')
    def test_should_add_s01e01_tag_if_none_is_present(self, mock_os):
        mockCurrentDirectory(mock_os, [])
        file = file_list.File.fromRelativePath('./test.txt')

        file.applyNextEpisodeTag()
        mock_os.rename.assert_called_with('./test.txt', './test.s01e01.txt')

    @mock.patch('next_episode.file_list.os')
    def test_should_add_next_tag_if_none_is_present(self, mock_os):
        mockCurrentDirectory(mock_os, [
                                      'oink.s01e03.mp4',
                                      'oink.s02e02.mp4',
                                  ])

        file = file_list.File.fromRelativePath('./test.txt')

        file.applyNextEpisodeTag()
        mock_os.rename.assert_called_with('./test.txt', './test.s02e03.txt')

    @mock.patch('next_episode.file_list.os')
    def test_should_do_nothing_if_tag_is_already_present(self, mock_os):
        mockCurrentDirectory(mock_os, [], 'test.s01e01.txt')

        file = file_list.File.fromRelativePath('./test.s01e01.txt')

        file.applyNextEpisodeTag()
        assert not mock_os.rename.called

class TestFileApplyNextSeasonTag:

    @mock.patch('next_episode.file_list.os')
    def test_should_add_s01e01_tag_if_none_is_present(self, mock_os):
        mockCurrentDirectory(mock_os, [])
        file = file_list.File.fromRelativePath('./test.txt')

        file.applyNextSeasonTag()
        mock_os.rename.assert_called_with('./test.txt', './test.s01e01.txt')

    @mock.patch('next_episode.file_list.os')
    def test_should_add_next_tag_if_none_is_present(self, mock_os):
        mockCurrentDirectory(mock_os, [
            'oink.s01e03.mp4',
            'oink.s02e02.mp4',
        ])

        file = file_list.File.fromRelativePath('./test.txt')

        file.applyNextSeasonTag()
        mock_os.rename.assert_called_with('./test.txt', './test.s03e01.txt')

    @mock.patch('next_episode.file_list.os')
    def test_should_do_nothing_if_tag_is_already_present(self, mock_os):
        mockCurrentDirectory(mock_os, [
            'oink.s02e02.mp4',
        ], 'test.s01e01.txt')

        file = file_list.File.fromRelativePath('./test.s01e01.txt')

        file.applyNextSeasonTag()
        assert not mock_os.rename.called

def mockCurrentDirectory(mock_os, present_files, basename='test.txt'):
    mock_os.path.basename.return_value = basename
    mock_os.path.abspath.return_value = './'+basename
    mock_os.path.dirname.return_value = '.'
    mock_os.listdir.return_value = present_files
