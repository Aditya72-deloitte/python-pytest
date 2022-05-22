# Merge two lists as shown below
# Given
# I / P
# list1 = ["Hello ", "take "]
# list2 = ["Dear", "Sir"]
# E / O
# ['Hello Dear', 'Hello Sir', 'take Dear', 'take Sir']


list_1 = ["Hello", "Take"]
list_2 = ["Dear", "Sir"]

list_3 = []

for i in range(len(list_1)):
    for j in range(len(list_2)):
        list_3.append(list_1[i] + " " + list_2[j])

print("list_1 : ", list_1)
print("list_2 : ", list_2)
print(list_3)
