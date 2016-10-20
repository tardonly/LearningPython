from wand.image import Image

with Image(filename='image12') as img:
    img.format = 'jpeg'
    img.save(filename = 'image21')
