from __future__ import print_function
from PIL import Image
import os, sys

for infile in sys.argv[1:]:
    f, e = os.path.splitext(infile)
    outfile = f + '.jpg'
    if infile != outfile:
        try:
            Image.open(infile).save(outfile)
        except IOError:
            print('Can not convert', infile)
