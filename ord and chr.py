b = ord('a') # it returns  ascii number to character 
# and if you want to convert ascii number to character you can use chr

chr(b)

print(b)



# book allocation
# 🎯 Goal of the count logic:
# We're trying to divide the books among k students such that no student gets more than mid pages.

# So we simulate giving books to students in order, keeping track of how many pages we've given to the current student.

# 👇 Let’s walk through this part of the code:
# python
# Copy
# Edit
# count = 1  # Start with first student
# current_sum = 0  # Pages given to the current student

# for pages in arr:
#     current_sum += pages

#     if current_sum > mid:
#         count += 1         # Need another student
#         current_sum = pages  # Start new student with current book
# 🔍 Example:
# python
# Copy
# Edit
# arr = [12, 34, 67, 90]
# k = 2
# Suppose we’re testing mid = 100:

# Give 12 → current_sum = 12

# Add 34 → current_sum = 46

# Add 67 → current_sum = 113 ❌ (too much)

# So, give 67 to next student → count = 2, current_sum = 67

# Add 90 → current_sum = 157 ❌

# Need another student → count = 3

# Here, count = 3 > k = 2 → So mid = 100 is too low.

# 🧠 Summary:
# count tracks how many students you needed to stay within the limit of mid pages.

# If count > k, the current mid is too low → increase it.

# If count <= k, it’s a valid solution → try reducing mid.