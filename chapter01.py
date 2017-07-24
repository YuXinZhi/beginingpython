import math
print(math.floor(32.9))
print(math.ceil(32.9))

tmp = 42
print('tmp = ' , tmp)
'''
32
33
tmp =  42
'''


#name = input('please input your name:')
#print(name +' welcome')

path = r'c:\nwindow'   #字符串前加r代表原始字符串，这样字符串中的\不会被转义
path2 = 'd:\\nwindow'
print(path)
print(path2)
'''
c:\nwindow
d:\nwindow
'''

print(r'c:\nwindow' '\\')
path3 = r'c:\nwindow' '\\'
print(path3)
'''
c:\nwindow\
c:\nwindow\
'''