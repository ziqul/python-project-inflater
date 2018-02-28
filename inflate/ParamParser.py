from optparse import OptionParser
from .NoParams import NoParams


class ParamParser(object):
    """
    ParamRetriver return parameters
    passed in command line
    """

    def __init__(self):
        super(ParamParser, self).__init__()

        self.params = dict()

        self.argnames = ['[project_name]']
        self.usage = 'usage: %prog'

        for argname in self.argnames:
            self.usage += ' ' + argname

        self.parser = OptionParser(self.usage)

    def get_params(self):
        (options, args) = self.parser.parse_args()

        if len(args) < len(self.argnames):
            self.parser.print_help()
            raise NoParams(
                "\n" +
                "Incorrect amount of positional parameters. " +
                "Expected {expected}, got {got}.".format(
                    expected=len(self.argnames), got=len(args)))

        self.params['project_name'] = args[0]

        return self.params
