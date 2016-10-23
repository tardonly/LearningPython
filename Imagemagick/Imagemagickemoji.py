import urllib2

from wand.image import Image
from wand.display import display


fg_url = 'http://i.stack.imgur.com/Mz9y0.jpg'
bg_url = 'http://i.stack.imgur.com/TAcBA.jpg'

bg = urllib2.urlopen(bg_url)
with Image(file=bg) as bg_img:
    fg = urllib2.urlopen(fg_url)
    with Image(file=fg) as fg_img:
        bg_img.composite(fg_img, left=400, top=250)
    fg.close()
    display(bg_img)
bg.close()
