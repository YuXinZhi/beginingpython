
def func(a,*rest,d):
    print(a,*rest,d)
    print(a)
    print(*rest)


func(1,2,3,4,d=5)

from math import sqrt
scope = {}
exec('sqrt=1', scope)  #scope命名空间
print(sqrt(4))
print(1/0)