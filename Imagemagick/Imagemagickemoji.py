import urllib2
import random

from wand.image import Image
from wand.display import display


fg_url = fg_url = 'http://emojidictionary.emojifoundation.com/img/emoji{}.jpg'.format(random.randint(1, 800)) #random emoji
bg_url = 'http://bit.ly/2ewFjd5'

bg = urllib2.urlopen(bg_url)
with Image(file=bg) as bg_img:
    fg = urllib2.urlopen(fg_url)
    with Image(file=fg) as fg_img:
        bg_img.composite(fg_img, left=214, top=160)
    fg.close()
    display(bg_img)
bg.close()
