# a = 5 


# if 6>a:
#     print('1.')
# elif 7>a:
#     print('2.')
#     if 3>=a:
#         print(3)
#     elif 10>a:
#         print(4)


# for i in range(10):
#     print(i)
# a = 1
# while a<=10:
#     print('Salam')
#     a = a + 1


# 86

# n = float(input()) # -6.8
# tam = int(n) #-6
# if n>0:
#     qaliq = n - tam
#     print(tam,qaliq)
# elif n < 0:
#     tam = tam - 1
#     qaliq = (-1*tam) + n
#     print(tam,qaliq)

# n = 5.6 - 5
# print(n)



# Sətirlər (String)

# username = '          elnur      '
# username =username.strip()
# print(username)


# Find method
# metin = 'salam necesen yaxshiyam'
# #        0123456789
# n = metin.find('s')
# print(n)

# print()

# "salam".upper()
# m = ''
# m.upper()
# str()

#  List (Array)

arr = [24,45,3,36,1,0]
#      0  1  2 3  4 

def maxsimum(arr):
    maxi = arr[0]
    for i in arr:
        if i>maxi:
            maxi = i
    return maxi

result = maxsimum(arr)
print(result)
# n = max(arr)
# print(n)

# for i in arr:
#     print(i)