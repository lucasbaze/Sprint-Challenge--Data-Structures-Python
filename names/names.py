import time

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []
# Time Compelexity for this is O(n*m).

# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)


# ATTEMPT 1

# Runtime for this is 0.0076 at max
# Time Complexity is O(max(n, m))
# But I'm using a dictionary... which isn't allowed? 

    # names_dict = {}
    # for x in range(0, len(names_1)):
    #     names_dict[names_1[x]] = x

    # for name_2 in names_2:
    #     if name_2 in names_dict:
    #         duplicates.append(name_2)

# Need to use a different data structure that doesn't have O(1) search? 

# ATTEMPT 2


end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish with no restrictions on techniques or data
# structures?
