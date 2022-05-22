# Map the dictionary in the following manner
# Keys = [‘Ten’, ‘Twenty’, ‘Thirty’]
# Value = [10,20,30]
# {'Ten': 10, 'Twenty': 20, 'Thirty': 30}

Keys = ["Ten", "Twenty", "Thirty"]
Value = [10, 20, 30]

Dict = dict(zip(Keys, Value))

print("Keys : ", Keys)
print("Value : ", Value)
print("Dictionary : ", Dict)
