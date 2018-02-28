import os


class FileContent(object):
    """docstring for FileContent"""

    def __init__(self, project_name):
        super(FileContent, self).__init__()
        self.project_name = project_name
        self.__filepath__ = os.path.realpath(__file__)

        self.__create_files_dict()

    def __create_files_dict(self):
        files_names = [
            './' + self.project_name + '/__init__.py',
            './' + self.project_name + '/resources/__init__.py',
            './test/__init__.py',
            './' + self.project_name + '.py',
            './requirements.txt',
            './LICENSE.md']

        self.fiels_dict = dict()

        for file_name in files_names:
            self.fiels_dict[file_name] = ''

        with open(
                os.path.join(
                    self.__filepath__,
                    '..',
                    'resources',
                    'sample_readme.md')) as f:
            self.fiels_dict['./README.md'] = f.read()

        with open(
                os.path.join(
                    self.__filepath__,
                    '..',
                    'resources',
                    '.gitignore_sample')) as f:
            self.fiels_dict['./.gitignore'] = f.read()

    def get_files_dict(self):
        return self.fiels_dict
