prices = {
    "banana" : 4,
    "apple" : 2,
    "orange" : 1.5,
    "pear" : 3
    }

purchased_items = [
    ["banana" , 5],
    ["orange" , 3]
    ]

for item in purchased_items:
    print("{0}\n quantity: {1}, \n unit price: {2}".format(item[0],item[1],prices[(item[0])]))

 
total = 0
for item in purchased_items:
    print("{0} Total value {1}".format(item[0], item[1]))
    total += item[1] * prices[(item[0])]

print("Total = ", total)
