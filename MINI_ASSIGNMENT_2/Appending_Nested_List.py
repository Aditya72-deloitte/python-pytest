# Given a nested list extend it by adding the sub list ["h", "i", "j"]
#  in such a way that it will look like the following list
# Given List:
# list1 = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]
# Sub List to be added = ["h", "i", "j"]
# Expected output:
# ['a', 'b', ['c', ['d', 'e', ['f', 'g', 'h', 'i', 'j'], 'k'], 'l'], 'm', 'n']

list_1 = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]
subList = ["h", "i", "j"]
print("List : ", list_1)
print("SubList : ", subList)

for i in range(0, len(subList)):
    (list_1[2][1][2]).append(subList[i])

print("Updated List : ", list_1)