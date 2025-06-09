#sytax for creating function
def printhello():
    print('hello world')
    
#this function will only be executed when i call this how to call
printhello()

#a =10 nothing will be printed cause you are just giving a reference of 10 assignment

# make this function dynamic by giving it parameter 
def greet(name):
    print("namaste "+name)
    
greet("hello") # passing value to parameter variable and value is called argument
greet("Rohit")

#you can also pass variable 
a = "virat kohli"
greet(a)# passing variable as argument to function paramter value

#function to multiply two variable
def multiply(a,b):
    mul =  a*b
    print(mul)
    
multiply(10,20)

#square of two function
#instead of printing function can also return a value and to get that value you have to call that function inside variable than only variable will store returned value
def square(a):
    result = a*a
    return result

value = square(2)#2 goes inside a
print(value)

#function is block of code that run whenever you call it 




    