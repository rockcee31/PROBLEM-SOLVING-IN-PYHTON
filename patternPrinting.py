"""
     *
    **
   ***
  ****
 *****
     
      """
# n = int(input("Enter Number of Rows :"))
# for i in range(n):
#     for j in range(n-i-1):
#         print(" ",end="")
#     for z in range(i+1):
#         print("*",end="")
#     print()


'''
   1
  22
 333
4444
'''

# for i in range(1,n+1):
#     for j in range(0,n-i):
#         print(" ",end="")
#     for z in range(i):
#         print(i,end="")    
#     print()


'''
   1
  12
 123
1234
'''

# for i in range(1,n+1):
#     for j in range(0,n-i):
#         print(" ",end="")
#     for z in range(1,i+1):
#         print(z,end="")
#     print()


'''
   A
  AB
 ABC
ABCD

'''

# for i in range(1,n+1):
#     for j in range(0,n-i):
#         print(" ",end="")
#     for z in range(ord('A'),ord("A")+i):
#         print(chr(z),end="")
#     print()


'''
*******
*** ***
**   **
*     *
**   **
*** ***
*******
'''

n = 7 # Number of rows

for i in range(n):
    if(i==0 or i==6):
        print(7*"*",end="")
    
    elif(i==1 or i==5):
        print(3*"*",end='')
        print(1*" ",end='')
        print(3*"*",end='')
    
    elif(i==3):
        print("*",end='')
        print(5*" ",end='')
        print("*",end='')
    elif(i==4 or i==2):
        print(2*"*",end='')
        print(3*" ",end='')
        print(2*"*",end='')




    print()        


'''
   *
  ***
 *****
*******
'''

for i in range(1,n+1):
    for j in range(n-i):
        print(" ",end='')
    for z in range(1,2*i):
        print("*",end="")

    print()

'''
    1
   12
  123
 1234
12345

'''