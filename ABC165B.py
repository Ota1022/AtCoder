x = int(input())
import math

num =  0
s = 100
while True :
    num += 1
    s += math.floor(s * 0.01)
    if  s >= x:
        break
    else:
        continue
print(num)

# x = int(input())
# j = 100
# time = 0
# while j < x:
#     j = int(j * 1.01)
#     time += 1
# print(time)