def extract_even(list):
    return[num for num in list if num % 2 == 0]

list = [1, 4, 5, -1, 10]
print(extract_even(list))

even_list = extract_even([1, 2, 5, -10, 9, 6])

if set(even_list) == set([2, -10, 6]):
    print("Your function is correct")
else:
    print("Ooops, bugs detected")
