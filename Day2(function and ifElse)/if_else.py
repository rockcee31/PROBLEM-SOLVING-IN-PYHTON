#by example explain if else 
#create a function which excepts the age and tells weather a person is elligible to vote or not

def elligibleToVote(age):
    if(age<0):
        print("invalid input")
    elif(age<18):
        print("you are elligible to vote")
    else:
        print('you are  elligible to vote')
    
# elligibleToVote(18)



#create a function to check if a number is even or odd
def isEvenOdd(num):
    if(num%2==0):
        print("it's Even Bro")
    else:
        print("it is odd brosky!")
        
    
isEvenOdd(0)

