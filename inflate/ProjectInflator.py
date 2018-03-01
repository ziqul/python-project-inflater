import os
from .FileContent import FileContent


class ProjectInflator(object):
    """
    Create required project structure
    """

    def __init__(self):
        super(ProjectInflator, self).__init__()

    def inflate(self, project_name):
        assert(type(project_name) is str)

        dirs = [
            './' + project_name,
            './' + project_name + '/resources/',
            './docs/',
            './test/']

        files_dict = FileContent(project_name).get_files_dict()

        list(map(self.__create_dir, dirs))
        list(
            self.__map_dict(
                self.__create_file_with_content, files_dict))

    def __create_dir(self, dirpath):
        if not os.path.exists(dirpath):
            os.makedirs(dirpath)

    def __create_file(self, filename):
        open(filename, 'a').close()

    def __create_file_with_content(self, filename, content):
        with open(filename, 'a') as f:
            f.write(content)

    def __map_dict(self, function, target_dict):
        assert(type(target_dict) is dict)

        for key in target_dict.keys():
            yield function(key, target_dict[key])
