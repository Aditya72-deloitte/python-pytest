# Convert Dictionary to list
# The original dictionary is : {‘HuEx	: [1, 3, 4], ‘is’: [7, 6], ‘best’: [4, 5]}
# The converted list is : [[‘HuEx, 1, 3, 4], [‘is’, 7, 6], [‘best’, 4, 5]]

originalDict = {'HuEx': [1, 3, 4], 'is': [7, 6], 'best': [4, 5]}
print("Original Dictionary : ", originalDict)

print()

convertedList = []

for k in originalDict.keys():
    convertedList.append(k)
    for l in originalDict[k]:
        convertedList.append(l)

print("Converted to List : ", convertedList)