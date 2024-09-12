
import math
a = math.sqrt(16)
print(a)


a = 5 
b = 6
c = 5
print("a + b") # a + b
print(a + b) # 11
print('a' + 'b') # ab

n = input()
print(type(n),n) 
n = 'Hello'
m = len(n)
for i in range(0,m):
    print(n[0])
print(n)

meyve = ['Alma','Armud','Mandalin','Portağal']
say = len(meyve)
# print(say)
for i in range(0,say):
    print(i)

a = 5
if a < 6:
    print('1.')
if a == 5:
    print("2.")
else:
    print('3.')




n = int(input())
if n > 2:
    if n%2 == 0:
        print(n-2)
    elif n%2 != 0:
        print(n-1)


a = int(input())
b = int(input())
c = int(input())
if a==b==c:
    print('Beraberterefli')
elif a!=b!=c:
    print('Müxtelif terefli')
else:
    print('Beraberyanli')



x=input()
y=[]
z=[]
n=0
for i in range(0,len(x),2):
    y.append(int(x[i]))
for j in range(len(y)):
    for i in y:
        if y[j]>i:
            print(j)
        elif y[j]==i:
            print(j)

    
print(y)
print(z)

n = input() #  1 2 3 4 5
a = n.split()
maxi = max(a)

print(maxi)

print(a)







