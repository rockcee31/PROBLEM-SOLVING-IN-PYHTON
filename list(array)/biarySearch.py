# list = [1,2,3,4,5,6,7]
# target = 8
# start=0
# end=len(list)-1

# while start<=end:
#     mid = (start+end)//2
#     if list[mid] == target:
#         print("Found at index",mid)
#         break
#     elif list[mid]<target:
#         start = mid+1
#     else:
#         end = mid-1
# else:
#     print("Not Found")



#binary search cana only be applied in sorted array or list with 1 side  increasing and 1 side decreasing or vice a versa
#binary search is a divide and conquer algorithm


list = [0,1,2,6,9,11,15]

start = mid = 0 
end= len(list)-1
index = 0
element = 0
while(start<=end):
    mid = (start+end)//2

    if(list[mid] > mid):
        index = mid 
        end = mid-1 

print(index)
