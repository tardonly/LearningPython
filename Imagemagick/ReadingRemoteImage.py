from __future__ import print_function
from urllib2 import urlopen
from wand.image import Image

response = urlopen('https://www.python.org/static/opengraph-icon-200x200.png')

try:
    with Image(file=response) as img:
        print('format =',img.format)
        print('size',img.size)
finally:
    response.close()
