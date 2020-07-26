1.
ans = [i for i in range(2000,3201,1) if i%7==0 and i%5!=0]
for j in ans:
    print(j,end=",")

2. 
user_input = input()
print(user_input[::-1])

3.
from math import pi
d = 12
V = (4*pi*(d/2)**3)/3
print(V)
