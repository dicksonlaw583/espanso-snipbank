import sys
import yaml
from common import *

def addTrigger(rootFile, trigger, snippet, reprint=False):
    '''
    Add a regular trigger to a match YAML file.
    '''
    data = getDefaultData()
    rectifiedSnippet = snippet.replace('^TAB^', "\t").replace('^ENTER^', "\n")
    with open(rootFile, 'r') as rootFh:
        data = yaml.load(rootFh, Loader=yaml.BaseLoader)
    data['matches'].append({"trigger": trigger, "replace": rectifiedSnippet})
    with open(rootFile, 'w') as rootFh:
        yaml.dump(data, rootFh)
    if reprint:
        print(rectifiedSnippet, end='')

if __name__ == '__main__':
    if not sys.argv[1]:
        exit(0)
    addTrigger(getSnipBankRootFile(), sys.argv[1], sys.argv[2], sys.argv[3] == 'paste')
