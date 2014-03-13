import os
import re

from enum import Enum

# directory of input files
inputpath = os.path.abspath(os.path.join(
    os.path.dirname(__file__), '..', 'input'))
# directory of input files
outputpath = os.path.abspath(os.path.join(
    os.path.dirname(__file__), '..', 'output'))
# types of sources and ressources
NodeType = Enum('NodeType', 'app jcl fex data other')
# main fex patterns
patterns = {'fexBeginEndComments': re.compile('^(?:-\*)\s*:\s*=*\s*\:\s*\n*$'),
            'fexInputTag': re.compile(
                '^(?:-\*)\s*:\s*(?:FICHIER)(?:S*)\s*(?:EN)\s*(?:ENTRE)(?:E*)'
                '(?:S*)\s*:\s*(\w+).*\n*$'),
            'fexOutputTag': re.compile(
                '^(?:-\*)\s*:\s*(?:FICHIER)(?:S*)\s*(?:EN)\s*(?:SORTIE)(?:E*)'
                '(?:S*)\s*:\s*(\w+).*\n*$'),
            'fexAddIO': re.compile('^(?:-\*)\s*:\s*:\s*(\w+).*\n*$'),
            'jclLine1': re.compile('^(?://).*\n*$'),
            'jclRunFex': re.compile('^(?://\*)\s*(?:REQUETE)\s*(\w+)\s*\n*$'),
            'jclApp': re.compile('^(?:\/\/)\s*(?:\w+)\s*(?:\w+)\s*\(\s*'
                                 '(\w+)\s*,.*\n*$'),
            }
