import os


def mock_current_directory(mock_os, present_files, basename='test.txt'):
    mock_os.path.basename.return_value = basename
    mock_os.path.abspath.return_value = './'+basename
    mock_os.path.dirname.return_value = '.'
    mock_os.listdir.return_value = present_files


def expected_file(file_name, replacements=None):
    return templated(expected_file_template(file_name), replacements)


def expected_file_template(file_name):
    dir_path = os.path.dirname(os.path.realpath(__file__))
    template_path = os.path.join(dir_path, 'expected_files', file_name)

    with open(template_path) as file:
        return file.read()


def templated(text, replacements=None):
    if replacements is None:
        replacements = {}

    for key in replacements:
        value = replacements[key]
        text = text.replace('%%'+key+'%%', value)

    return text


def mocked_handle(mock_open):
    return mock_open.return_value.__enter__.return_value
