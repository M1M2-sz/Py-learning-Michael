import numpy as np
from PIL import Image, ImageDraw
import sys

sys.setrecursionlimit(150000)

def fillarea(baba,x,y):
  if (x<0) or (y<0) or (x>=270) or (y>=400):#270x400 - image size
    return 0
  valuee=baba[y,x]
  if valuee[1]==255:# search green 
    return 0
  baba[y,x]=[0,255,0];#green fill 
  area=1 
  for y1 in range(3):#range 3 step
    for x1 in range(3):#range 3 step
      area=area+fillarea(baba,x+x1,y+y1)#(recursion) - function restart with a new param
  return area

image_1 = Image.new('RGB', (270, 400), (255, 255, 255))
draw = ImageDraw.Draw(image_1)
#Figure 1
draw.rectangle((125, 35, 110, 20), fill=(10, 10, 10))
#Figure 2
draw.rectangle((80, 40, 90, 50), fill=(10, 10, 10))
#Figure 3
axy = (        
            (125, 50),
            (100, 50),
            (100, 75),
            (125, 75)        
      )
draw.polygon(xy=axy, fill='black', outline=(10, 10, 10))

baba = np.array(image_1)

#Method3
count=0
totalarea=0
for y in range(image_1.height):
 for x in range(image_1.width):
  valuee=baba[y,x]
  if valuee[0]!=0 and valuee[1]!=255 and valuee[2]!=0: #full search green fill 
   count+=1
   area=fillarea(baba,x,y)
   print(' i have found ',count,' figure with area = ',area)
   totalarea+=area
print('total area is ',totalarea)

img = Image.fromarray(baba)
img.show()

