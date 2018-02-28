import sys
from project_inflater.ParamParser import ParamParser
from project_inflater.ProjectInflator import ProjectInflator
from project_inflater.NoParams import NoParams


parser = ParamParser()
inflator = ProjectInflator()

try:
    params = parser.get_params()
except NoParams as np:
    sys.exit(np.args)

inflator.inflate(params['project_name'])
