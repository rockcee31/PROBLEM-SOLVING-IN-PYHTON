'''Sorting means arranging the elements of a list in a certain order'''

'''Selection Sort
it is a simple algorithm that find the minimum element in the list(array) and swap it with the first element'''

unordered_List = [64, 25, 12, 22, 11]
# def selectonSort(list):
#     for i in range(len(list)):
#         min_index = i
#         for j in range(i,len(list)):
#             if list[j] < list[min_index]:
#                 min_index = j
#         list[i],list[min_index] = list[min_index],list[i]
#     return list

# print(selectonSort(unordered_List))




'''Bubble Sort
it is a simple algorith that repeately steps through the list, compares adjacent elements and swaps them if they are in worng order '''

# def bubblesort(list):
#     n=len(list)
#     for i in range(n):
#         for j in range(n-i-1):
#             if list[j] > list[j+1]:
#                 list[j],list[j+1] = list[j+1],list[j]
#     return list

# print(bubblesort(unordered_List))


'''Insertion Sort
it is a simple algorith that builds a sorted array by taking one element at a time and inserting it into the  correct positon by comparing its value with the previous  elements in the sorted array if that exists else it will be inserted at the beginning of the array'''

# for i in range(len(list)):
#     for j in range(len(list)-i-1):
#         if list[j] > list[j+1]:
#             list[j],list[j+1] = list[j+1],list[j]

#     print(list)