"::::::::::::::::::::::::::: Star Pattern :::::::::::::::::::::::::::"


'1  Single star'
# print("*")
'''
*
'''

'2  Four star'
# print("*" * 4)
'''
****
'''



'3  Print n star on same line'
# n = 8
# for i in range(n):
#     print("*", end="")
# print()
'''
********
'''





'4  Print Square of Stars (n x n Stars)'
# n = 4
# for i in range(0,n):
#     for j in range(0,n):
#         print("*",end="") 
#     print()

'''
****
****
****
****
'''





'5  Print an Increasing Triangle of Stars'
# n = 5
# for i in range(1,n):
#     for j in range(i):
#         print("*",end="")
#     print()

'''
*
**
***
****
'''




'6  Print an Decreasing Triangle of Stars'
# n = 5
# for i in range(n,0,-1):
#     for j in range(i):
#         print("*",end="")
#     print()

'''
****
***
**
*
'''



'7  Print a Right-Aligned Triangle of Stars'
# n = 5
# for i in range(n):

#     # Print spaces
#     for k in range(n-i-1):
#         print(" ", end="")

#     # print star
#     for j in range(i):
#         print("*",end="")
#     print()

'''
   *
  **
 ***
****
'''



'8  Print Stars in Even Numbers (2, 4, 6, 8, 10)'
# n = 4
# for i in range(1,n):
#     for j in range(2*i):
#         # print(f"I : {i}, J : {j}")
#         print("*", end="")
#     print("")

'''
**
****
******
********
**********
'''


'9  Print Stars in Odd Numbers (1, 3, 5, 7, 9)'
# n = 4
# for i in range(n):
#     for j in range(2*i+1):
#         print("*", end="")
#     print("")

'''
*
***
*****
*******
*********
'''


'10 Print a Centered Pyramid of Stars'
# n = 5
# for i in range(n):

#     # Print spaces
#     for k in range(n-i-1):
#         # print(f"k{k}")
#         print(" ",end=f"")

#     # print star
#     for j in range(2*i+1):
#         # print(f"j{j}")
#         print("*",end=f"")

#     print()

'''
    *
   ***
  ******
 ********
**********
'''




'11 Print Stars and Spaces Alternating (Stars and Blank Spaces)'
# n = 5
# for i in range(n):

#     # Print spaces
#     for k in range(n-i-1):
#         # print(f"k{k}")
#         print("b",end="")

#     # print star
#     for j in range(2*i+1):

#         if j%2 == 0:
#             print("*",end="")
#         else:
#             print("b",end="")
#     print()


'''
bbbb*
bbb*b*
bb*b*b*
b*b*b*b*
*b*b*b*b*
'''



'12 Print Stars and Spaces Alternating (Stars and Blank Spaces)'
# n = 6
# for i in range(1,n+1):
#     for j in range(1,i):
#         print(j,end="")
#     print()

'''
1
12
123
1234
12345
'''


'13 Print Repeated Numbers per Row (Same Number Repeated)'
# n = 6
# for i in range(n+1):
#     for j in range(i):
#         print(i,end="")
#     print()

'''
1
22
333
4444
55555
666666
'''



'14 '
# n = 6
# num = 1
# for i in range(1,n):
#     for j in range(i):
#         print(num, end=" ")
#         num+=1
#     print()

'''
1
2 3
4 5 6
7 8 9 10
11 12 13 14 15 
'''

'15 '
# n = 10
# num = 1
# for i in range(1,n):
#     for j in range(i):
#         print(num, end=" ")
#         num+=1
#         if num == 10:
#             num = 0
#     print()

'''
1
2 3
4 5 6
7 8  9 0
1 2 3 4 5
6 7 8 9 0 1
2 3 4 5 6 7 8 
'''



'16 '
# n = 10
# num = 1
# for i in range(1,n):
#     for j in range(i):
#         if num %2 == 0:
#             stat = 0
#         else:
#             stat = 1
#         print(stat, end=" ")
#         num+=1
#         if num == 10:
#             num = 0
#     print()

'''
1
0 1 
0 1 0
1 0 1 0
1 0 1 0 1
0 1 0 1 0 1 
'''



'17 '
# n = 6
# ascii_val = 65
# for i in range(1,n):
#     for j in range(i):
#         print(chr(ascii_val), end=" ")
#         ascii_val +=1
#     print()

"""
A
B C 
D E F
G H I J
K L M N O
"""



'18 '
# n = 6
# ascii_val = 65
# for i in range(1,n):
#     for j in range(i):
#         print(chr(ascii_val), end=" ")
#     ascii_val +=1
#     print()

"""
A
B B 
C C C
D D D D
"""



'19 '
# n = 5
# ascii_val = 65
# for i in range(1,n):
#     for j in range(i):
#         print(chr(ascii_val+j), end=" ")
#     print()

"""
A
A B 
A B C
A B C D
"""





'Factorial'
def fac(n):
    if n<=1:
        return 1
    
    return n*fac(n-1)
# print(fac(4))


'Fibonacci'
# def fib(n):
#     if n <=1:
#         return n
#     return fib(n-1)+fac(n-2)
# print(fib(5))



# st = "YASHJAIN"
# a = ''
# n = len(st)
# for i in range(n-1,-1,-1):
#     a+=st[i]
# print(a)



a = [3,3,42,4,2,5,67,3,2,46]
b = []

while a:
    min = a[0]
    for i in a:
        if i < min:
            min = i
    b.append(min)
    a.remove(min)
    
print(b)                  












     


