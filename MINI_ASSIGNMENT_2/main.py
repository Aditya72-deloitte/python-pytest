# Problem  – Data Structures
#
# Return all the duplicate value list of arraylist s from
# Input:
# [[1,1,3,2],[9,8,8,1],[0,4,5,0,0,1,4]]
# Output: 
# 1 -> 2
# 8 -> 2
# 0 -> 3, 4 -> 2

Arraylist = [[1, 1, 3, 2],
             [9, 8, 8, 1],
             [0, 4, 5, 0, 0, 1, 4]
             ]
result = {}

for i in range(len(Arraylist)):
    res = {}
    for j in Arraylist[i]:
        res[j] = Arraylist[i].count(j)
    print("in res ", res)
    result[i] = res
    print("in result ", result)

for i in result.keys():
    print()
    for j in result[i].keys():
        if result[i][j] > 1:
            print(j, "->", result[i][j], " ", end="")
