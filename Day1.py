''' prime Number
a = int(input("enter a number: "))

for i in range(2,a):
    if(a%i == 0):
        print("not a prime")
        break;
    
print(f'{a} is a prime number')     '''

# logic - devide that number from 2 to number below it n-1

''' fibbonacci series'''
fibonacci_series = [0,1]
first_value =0
second_value = 1
current_value = None
 
b= int(input("enter a number :"))


for i in range(3,b+1):
    current_value= first_value+second_value;
    fibonacci_series.append(current_value)
    first_value = second_value
    second_value = current_value


print(",".join(fibonacci_series))
# c=int(3>2>1)
# print(c)


'''
The approach you're using is Bubble Sort, where:

You repeatedly compare adjacent elements (arr[j] and arr[j+1])

And swap them if they are in the wrong order (arr[j] > arr[j+1])

Each pass pushes the largest unsorted element to the end — like bubbles rising up 🌊



class Solution:
    # Function to sort an array of 0s, 1s, and 2s
    def sort012(self, arr):
        # code here
        n= len(arr)
        for i in range(n):
            for j in range(n-i-1):
                if(arr[j]>arr[j+1]):
                    temp = arr[j]
                    arr[j] = arr[j+1]
                    arr[j+1]= temp
                
        
        return arr
        
        
        '''