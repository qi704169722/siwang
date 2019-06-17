#1行实现阶乘之和
from functools import reduce
#print(reduce(lambda x, y: x + y, [1, 3, 4, 6, 8]))
print(reduce(lambda x,y:x+y,[reduce(lambda x,y:x*y,range(1,i+1)) for i in range(1, int(input())+1)]))

