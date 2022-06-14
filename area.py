import numpy as np
## Импортируем библиотеку pithon под названием numpy(numerical python extensions),
# под названием  np для общепринятости (все так делают что бы не писать полньстью
# numpy - проще написать np) 
from PIL import Image, ImageDraw
## Импортируем библиотеку Pillow, с модулями Image и ImageDraw
# Библиотека изображений Python, или PIL (Python Imaging Library) 
# нужна для обработки графики в Python.
# Image это класс определенный в модуле PIL.
# ImageDraw это модуль, который  позволяет рисовать 
# используя или систему относительных координат, или методы рисования 
# которые начинаются на draw:
# draw.polygon , draw.ellipse , draw.rectangle , и прочие.
# То есть из PIL мы импортируем класс Image, и модуль ImageDraw
import sys
## sys это модуль который обеспечивает доступ к некоторым переменным и функциям, 
# взаимодействующим с интерпретатором python.
# На пример все с началом sys. :
# sys.setrecursionlimit(), sys.getrecursionlimit() 
print(sys.getrecursionlimit())
## 
sys.setrecursionlimit(150000)

def fillarea(a,x,y):
  if (x<0) or (y<0) or (x>=a.shape[1]) or (y>=a.shape[0]): #borders
    return 0
  val=a[y,x]
  if val[0]==255: #just R
    return 0
#  print('x=',x,'y=',y)
#  a[x,y]=[255,255,255]; #clear point as White
  a[y,x]=[255,0,0]; #clear point as Red (just for visual purpose)
  area=1 #at least 1 point is filled
  for _y in range(-1,2):
    for _x in range(-1,2):
      area=area+fillarea(a,x+_x,y+_y)
  return area;

im = Image.new('RGB', (270, 400), (255, 255, 255))
draw = ImageDraw.Draw(im)
draw.rectangle((0, 11, 20, 30), fill=(0, 0, 0))
draw.rectangle((30, 40, 40, 45), fill=(0, 0, 0))


_xy = (        
            (350, 450),
            (50+100, 50+20),
            (50+10+20,50+20+10),
            (50+10+20+-20, 50+20+10+10),
            (50+10+20+-20+10,50+20+10+10+20),
            (50+10+20+-20+10+-20,50+20+10+10+20+-20)
      )

#draw.polygon(xy=_xy, fill='blue', outline=(0, 0, 0),width=1)
draw.polygon(xy=_xy, fill='blue', outline=(0, 0, 0))

#im.show()

a = np.array(im)
#np.setflags(write=1)

#Method1
count=0
for y in range(im.height):
 for val in a[y]:   #every point in y row (x)
  if (val[0]!=255): #check just R from RGB (it is enough)
   count+=1
print('area =',count)

#Method2
count=0
for y in range(im.height):
 for x in range(im.width):
  val=a[y,x]
  if (val[0]!=255): #check just R from RGB (it is enough)
   count+=1
print('area =',count)

#Method3
count=0
totalarea=0
for y in range(im.height):
 for x in range(im.width):
  val=a[y,x]
  if val[0]!=255: #just R
   count+=1
   area=fillarea(a,x,y)
   print(' i have found ',count,' figure with area = ',area)
   totalarea+=area
print('total area is ',totalarea)


img = Image.fromarray(a)
img.show()
