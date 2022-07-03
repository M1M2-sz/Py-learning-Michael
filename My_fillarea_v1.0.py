import numpy as np
from PIL import Image, ImageDraw

image_1 = Image.new('RGB', (270, 400), (255, 255, 255))
draw = ImageDraw.Draw(image_1)
draw.rectangle((125, 35, 110, 20), fill=(20, 30, 45))
draw.rectangle((80, 40, 90, 50), fill=(25, 35, 40))

A_xy = (        
            (125, 50),
            (100, 50),
            (100, 75),
            (125, 75)        
      )
draw.polygon(xy=A_xy, fill='black', outline=(10, 20, 25))

a = np.array(image_1)
#np.setflags(write=1)

img = Image.fromarray(a)
img.show()




