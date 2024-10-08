a = 5
b = 7

if a != b:
    print("1.")
else:
    print('2.')

n = "Hello" 

for i in range(100):
    print(n)

start = 1
while start <= 100:
    print(n)
    start = start + 1

print(n)
print(n)
print(n)
print(n)
print(n)
print(n)
print(n)
print(n)
print(n)
print(n)


# 66   Dövrlər

a = "12"
b = "a"

print(a + b)

n = int(input()) #2564 tam ədəd oldu
n = str(n)  # yenidən sətir oldu
uzunluq = len(n) # 4
for i in range(0,uzunluq):
    print(n[i])

# 67

# 1-ci üsul
n = int(input()) # 2345
b = n//10%10 #4
a = n//100%10 #3
if b%2 != 0:
    print(a*b)
elif b%2 == 0:
    print(a+b)

# 2 - ci üsul

n = input() # 2345
            # 0123 indexidir
a = n[1] #3
b = n[2] #4
if int(b)%2 == 0:
    print(int(a)+int(b))
else:
    print(int(a)*int(b))

# 68

n = int(input())
s = 0
for i in range(1,n+1):
    s = s + 1/i**2
print(s)


# List ------------------------------------------------
        #  0        1       2         3
meyve = ['Alma','Armud', 'Gilas', "Portağal"]
print(meyve[2])
length = len(meyve)
print(length)
for x in range(0,length):
    print(meyve[x])


# Maximum ədədin tapılması

list = [2,3,4,5,15,1,35,2,3,4]
maxi = list[0]
# print(maxi)
for i in list:
    if i>maxi:
        maxi = i
print(maxi)

print(max(list))








