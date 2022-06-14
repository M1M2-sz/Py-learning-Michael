import numpy as np
## Импортируем библиотеку python под названием numpy(numerical python extensions),
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
## .getrecursionlimit это функция которая возвращает текущее значение предела рекурсии,
#  максимальную глубину стека интерпретатора Python. 
# Этот предел предотвращает бесконечную рекурсию от переполнения стека языка C 
# и сбоя Python. Это значение может быть установлено с помощью sys.setrecursionlimit().
sys.setrecursionlimit(150000)
# Функция sys.setrecursionlimit() устанавливает максимальную глубину стека 
# интерпретатора Python для ограничения. Этот предел предотвращает бесконечную 
# рекурсию от переполнения стека языка C и сбоя Python. 
# Максимально возможный предел зависит от платформы. 
def fillarea(a,x,y): ## Создаем функцию fillarea , с переменными x, y (которые принимают позже тип числа), и массивом a
  if (x<0) or (y<0) or (x>=a.shape[1]) or (y>=a.shape[0]): #borders
    return 0
    ## Описание условия:
    # Если (x<0), или (y<0), или (x>=a.shape[1]) - [функция shape возвращает
    #  форму массива. Массив представляет собой кортеж целых чисел.] 
    # В данном случае условие (x>=a.shape[1]) такое: x>= индекса 1 в массиве a
    # ... или условие (y>=a.shape[0]) - такое: y>= индекса 0 в массиве a
    # то return 0       
  val=a[y,x]  # переменная val  принимает значения индексов y и x от a
  if val[0]==255: # если индекс 0 val равен 255 то
    return 0 # вернуть 0 
#  print('x=',x,'y=',y)
#  a[x,y]=[255,255,255]; #clear point as White
  a[y,x]=[255,0,0]; #clear point as Red (just for visual purpose) # Если индексы x и y от a = 255,0,0 то
  area=1 #at least 1 point is filled # точка заполнена
  # создаем двойной цикл
  for _y in range(-1,2): #  для у в диапазоне -1, 2 
    for _x in range(-1,2):#  для х в диапазоне -1, 2 
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
# обнуляем переменную count
for y in range(im.height):# Для y в диапазоне (im.по высоте)
 for val in a[y]:# для val в a с индексом [y]
  if (val[0]!=255):# если индекс 0 переменной val [red] не равен 255 то :
   count+=1# счетчик +1
print('area =',count)# выводим строку и значение count

#Method2
count=0
# обнуляем переменную count
for y in range(im.height):# Для y в диапазоне (im.по высоте)
 for x in range(im.width):# Для х в диапазоне (im.по длинне)
  val=a[y,x]# переменная val = индексы a [y,x]
  if (val[0]!=255):# если индекс 0 переменной val [red] не равен 255 то :
   count+=1# счетчик +1
print('area =',count)# выводим строку и значение count

#Method3
count=0
# обнуляем переменную count
totalarea=0
# обнуляем переменную totalarea
# создаем двойной цикл
for y in range(im.height): # Для y в диапазоне (im.по высоте)
 for x in range(im.width): # Для х в диапазоне (im.по длинне)
  val=a[y,x] # переменная val = индексы a [y,x]
  if val[0]!=255: # если индекс 0 переменной val [red] не равен 255 то :
   count+=1 # счетчик +1
   area=fillarea(a,x,y) # переменной area присваиваем значения от fillarea а именно a, x, y
   print(' i have found ',count,' figure with area = ',area) # выводим строку и значение count, потом еще строку и значение area
   totalarea+=area # к переменной totalarea добавляем значение от area
print('total area is ',totalarea) # выводим строку и значение totalarea


img = Image.fromarray(a)
img.show()
