from next_episode import file_list

class TestFileList:
    FILENAMES_NO_ENTRIES = [
        'teaser.mp4',
        'episode 1.mp4',
        'episode 2.mp4',
    ]

    # test_it_should_find_highest_episode_as_next_episode

    def test_it_should_find_season_1_if_files_dont_have_any_entries(self):
        fileList = file_list.FileList.fromFilenames(self.FILENAMES_NO_ENTRIES)
        assert fileList.currentSeason() == 1

    def test_it_should_find_next_season_1_if_files_dont_have_any_entries(self):
        fileList = file_list.FileList.fromFilenames(self.FILENAMES_NO_ENTRIES)
        assert fileList.nextSeason() == 1

    def test_it_should_find_episode_0_if_files_dont_have_any_entries(self):
        fileList = file_list.FileList.fromFilenames(self.FILENAMES_NO_ENTRIES)
        assert fileList.currentEpisode() == 0

    def test_it_should_find_next_episode_1_if_files_dont_have_any_entries(self):
        fileList = file_list.FileList.fromFilenames(self.FILENAMES_NO_ENTRIES)
        assert fileList.nextEpisode() == 1

    def test_it_should_find_highest_season_as_current_season(self):
        fileList = file_list.FileList.fromFilenames([
            'teaser.s00e01.mp4',
            'episode 1.s02e01.mp4',
            'episode 2.s01e02.mp4',
        ])
        assert fileList.currentSeason() == 2

    def test_it_should_find_highest_season_plus_one_as_next_season(self):
        fileList = file_list.FileList.fromFilenames([
            'teaser.s00e01.mp4',
            'episode 1.s02e01.mp4',
            'episode 2.s01e02.mp4',
        ])
        assert fileList.nextSeason() == 3

    def test_it_should_find_the_highest_episode_of_the_highest_season(self):
        fileList = file_list.FileList.fromFilenames([
            'teaser.s00e01.mp4',
            'episode 1.s02e01.mp4',
            'episode 2.s01e02.mp4',
        ])
        assert fileList.currentEpisode() == 1

    def test_it_should_find_the_highest_episode_plus_one_of_the_highest_season_as_next_episode(self):
        fileList = file_list.FileList.fromFilenames([
            'teaser.s00e01.mp4',
            'episode 1.s02e01.mp4',
            'episode 2.s01e02.mp4',
        ])
        assert fileList.nextEpisode() == 2
