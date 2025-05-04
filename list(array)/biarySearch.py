list = [1,2,3,4,5,6,7]
target = 8
start=0
end=len(list)-1

while start<=end:
    mid = (start+end)//2
    if list[mid] == target:
        print("Found at index",mid)
        break
    elif list[mid]<target:
        start = mid+1
    else:
        end = mid-1
else:
    print("Not Found")
