#wrtie a function that searches for an element in an array and returns the index if element not fount return -1

# name = ["rohit","mohit","sohit","tohit"]
# target = str(input(">"))
# length = len(name)
# index = -1
# for i in range(length):
#     if(name[i] == target):
#         index = i
# print(index)
    
    
# writr a function that finds number  of negative element in arr

# def count_of_negatives(arr):
#     negative_num = 0
#     length = len(arr)
#     for i in range(length):
#         if(arr[i]<0):
#             negative_num+=1
#     print(negative_num)
# count_of_negatives([2,-9,17,0,1,-10,-4,8])
    
    

#write a function that return largest number in array
def largest_in_array(arr):
    largest = arr[0]
    for i in range(len(arr)):
        if(arr[i]>largest):
            largest=arr[i]
    print(largest)
        
    

largest_in_array(arr =[2,-9,17,0,1,-10,-4,8])