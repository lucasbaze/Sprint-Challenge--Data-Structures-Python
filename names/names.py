import time
from binary_search_tree import BinarySearchTree


f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

start_time = time.time()
duplicates = []

# Time Compelexity for this is O(n*m).

# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)

# ATTEMPT 1
# Let's use a binary search tree
# This will have Time Complexity of O(log(n)) for insertion and O(log(n)) for look up
# So in total this is O(log(n) + log(n)) => O(log(n))
bst = BinarySearchTree(names_1[0])

# Slice the first element off since it's already included in the BinarySearchTree
for name_1 in names_1[1:]:
    bst.insert(name_1)

for name_2 in names_2:
    if bst.contains(name_2):
        duplicates.append(name_2)



end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish with no restrictions on techniques or data
# structures?

start_time = time.time()

duplicates_stretch = []

# STRETCH ATTEMPT 1

# Runtime for this is 0.0076 at max
# Time Complexity is O(max(n, m))

names_dict_stretch = {}
for x in range(0, len(names_1)):
    names_dict_stretch[names_1[x]] = x

for name_2 in names_2:
    if name_2 in names_dict_stretch:
        duplicates_stretch.append(name_2)


end_time = time.time()
print (f"{len(duplicates_stretch)} duplicates:\n\n{', '.join(duplicates_stretch)}\n\n")
print (f"runtime: {end_time - start_time} seconds")


# ------- STRETCH ATTEMPT 2 ---------


start_time = time.time()

# STRETCH ATTEMPT 2
duplicates_stretch_2 = list(set(names_1) & set(names_2))


end_time = time.time()
print (f"{len(duplicates_stretch_2)} duplicates:\n\n{', '.join(duplicates_stretch_2)}\n\n")
print (f"runtime: {end_time - start_time} seconds")