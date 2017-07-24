str1 = 'abcde'
str2 = str1[2:-4]
print(str2=='')

tmp = '123456789'
print(tmp[::-1])
print(tmp[-1:-4:-1])

n = [8,9,0]
s = ['3','4',5]
print(n+s)

#print('index ' ,s.index('2'))

x = [2,9,4,5,3]
y = x
y.sort()
print('x=',x,'y=',y)
'''
x= [2, 3, 4, 5, 9] y= [2, 3, 4, 5, 9]
'''
x = [2,9,4,5,3]
y = x[:]
y.sort()
print('x=',x,'y=',y)
'''
x= [2, 9, 4, 5, 3] y= [2, 3, 4, 5, 9]
'''