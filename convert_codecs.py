#!/usr/env python
# -*- coding: utf-8 -*-

"""Convert file codecs

Usage:
    convert_codecs.py <sourceFile> <targetFile> <sourceEncoding> <targetEncoding>
    convert_codecs.py (-h | --help)

"""

import codecs
from docopt import docopt

__version__ = '0.1'
__author__ = 'Honghe'

BLOCKSIZE = 1024**2 # size in bytes

def convert(sourceFile, targetFile, sourceEncoding, targetEncoding):
    with codecs.open(sourceFile, 'rb', sourceEncoding) as sfile:
        with codecs.open(targetFile, 'wb', targetEncoding) as tfile:
            while True:
                contents = sfile.read(BLOCKSIZE)
                if not contents:
                    break 
                tfile.write(contents)

if __name__ == '__main__':
    arguments = docopt(__doc__)
    sourceFile = arguments['<sourceFile>']
    targetFile = arguments['<targetFile>']
    sourceEncoding = arguments['<sourceEncoding>']
    targetEncoding = arguments['<targetEncoding>']
    convert(sourceFile, targetFile, sourceEncoding, targetEncoding)
