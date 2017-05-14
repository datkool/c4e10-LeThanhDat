clothes = ["T-Shirt" , "Sweater"]

print(clothes)

while True:
    
    action = input("Welcome to our shop, what do you want (C, R, U, D)? ")
    action = action.upper()
    if action == "C":
        item = input("Item: ")
        clothes.append(item)
        print(clothes)
    elif action == "R":
        print(clothes)
    elif action == "U":
        item_no = int(input("Update position? "))
        item = input("New item? ")
        clothes.insert(item_no, item)
        print(clothes)
    if action == "D":
        del_item = int(input("Delete position? "))
        clothes.pop(del_item)
        print(clothes)
    else:
        print("Nhap lai de")
    
