# Rename key city to location in the following dictionary
# sampleDict = {
#   "name": "Kelly",
#   "age":25,
#   "salary": 8000,
#   "city": "New york"
# }

sampleDict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"
}
print("Before Editing: ", sampleDict)
print()

sampleDict["location"] = sampleDict["city"]
del (sampleDict["city"])

print("After Editing: ",sampleDict)
