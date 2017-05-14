your_name = input("Your name: ")
sheep_size = [9, 4, 270, 150, 35, 69, 88]

print("Hello, My name is {0} and these are my ship size : {1}".format(your_name,sheep_size))

print("Now my biggest sheep has size {0} let's shear it".format(max(sheep_size)))

while True:
    
    month = int(input("Month = "))
    for i in range(month):
        month_no = month + 1
        print("Month: ", i)
        add_sheep = [ x + i * 50 for x in sheep_size]
        print("{0} month has passed, now here is my flock ".format(i + 1), add_sheep)
        big_sheep = max(add_sheep)
        print("my biggest sheep has size {0} let's sheer it".format(big_sheep))
        add_sheep.remove(big_sheep)
        print("After shearing, here is my flock ", add_sheep)
    print("My flock has size in total: ", sum(add_sheep))
    print("I would get {0} $".format(sum(add_sheep)*2))
