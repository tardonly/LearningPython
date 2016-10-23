import urllib2

from wand.image import Image
from wand.display import display


fg_url = 'http://bit.ly/2ek2g6j'
bg_url = 'http://bit.ly/2ewFjd5'

bg = urllib2.urlopen(bg_url)
with Image(file=bg) as bg_img:
    fg = urllib2.urlopen(fg_url)
    with Image(file=fg) as fg_img:
        bg_img.composite(fg_img, left=320, top=240)
    fg.close()
    display(bg_img)
bg.close()
