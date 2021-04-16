from PIL import Image
import numpy

size = (28, 28)

# convert all images to greyscale + resize

images = [ Image.open("checkpoint3_0.PNG"), 
           Image.open("checkpoint3_1.PNG"),
           Image.open("checkpoint3_2.PNG") ]


for im in images:
    edit = im.convert('L').resize(size) #also invert and scale
    name = im.filename.strip('.PNG')
    name = name + "_edited.PNG"
    edit.save(name)
