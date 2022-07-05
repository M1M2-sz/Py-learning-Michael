import numpy as np
from PIL import Image, ImageDraw
import sys

sys.setrecursionlimit(150000)

def fillarea(baba,x,y):
  if (x<0) or (y<0) or (x>=baba.shape[1]) or (y>=baba.shape[0]):
    return 0
  valuee=baba[y,x]
  if valuee[1]==255:# search green 
    return 0
  baba[y,x]=[0,255,0];#green fill 
  area=1 
  for y1 in range(-1,2):#range 3 step
    for x1 in range(-1,2):#range 3 step
      area=area+fillarea(baba,x+x1,y+y1)#(recursion) - function restart with a new param
  return area

raw_path =  sys.argv[1]
path = raw_path.replace('\\', '/').replace('"',"")
image_1 = Image.open(path,'r')

baba = np.array(image_1)

#Method3
count=0
totalarea=0
for y in range(image_1.height):
 for x in range(image_1.width):
  valuee=baba[y,x]
  if valuee[0]!=255 or valuee[1]!=255 or valuee[2]!=255:
   count+=1
   area=fillarea(baba,x,y)
   print(' i have found ',count,' figure with area = ',area)
   totalarea+=area
print('total area is ',totalarea)

img = Image.fromarray(baba)
img.show()


