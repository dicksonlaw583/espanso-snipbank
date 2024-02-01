import sys
import yaml
from common import *

def addTrigger(rootFile, trigger, snippet):
    '''
    Add a regular trigger to a match YAML file.
    '''
    data = getDefaultData()
    with open(rootFile, 'r') as rootFh:
        data = yaml.load(rootFh, Loader=yaml.BaseLoader)
    data['matches'].append({"trigger": trigger, "replace": snippet})
    with open(rootFile, 'w') as rootFh:
        yaml.dump(data, rootFh)

if __name__ == '__main__':
    if not sys.argv[1]:
        exit(0)
    if sys.argv[3] == 'paste':
        print(sys.argv[2], end='')
    addTrigger(getSnipBankRootFile(), sys.argv[1], sys.argv[2])
