import os

path = '//STOCK/LIBRARY/Художественная/Магия фэнтези'

def checkFile(path, level = 1):
    print('Level = ', level, 'Content: ', os.listdir(path))
    for i in os.listdir(path):
        if os.path.isdir(path + '//' + i):
            print('Level down', path + '//' + i)
            checkFile(path + '//' + i, level + 1)
            print('Get back to', path)
checkFile(path)
