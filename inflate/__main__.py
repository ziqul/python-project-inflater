import sys
from .ParamParser import ParamParser
from .ProjectInflator import ProjectInflator
from .NoParams import NoParams


parser = ParamParser()
inflator = ProjectInflator()

try:
    params = parser.get_params()
except NoParams as np:
    sys.exit(np.args)

inflator.inflate(params['project_name'])
