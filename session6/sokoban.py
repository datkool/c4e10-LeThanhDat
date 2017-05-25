#pusher
pusher_x = 5
pusher_y = 5

#box
box1 = {
    "x": 2,
    "y": 2
    }

box2 = {
    "x": 7,
    "y": 2
    }

box3 = {
    "x": 5,
    "y": 8
    }

boxes = [box1, box2, box3]

#destination
dest1 = {
    "x": 0,
    "y":1
    }

dest2 = {
    "x": 9,
    "y": 0
    }

dest3 = {
    "x": 8,
    "y": 9
    }

destination = [dest1, dest2,dest3]

#map

size_x = 10
size_y = 10

def check_overlap(x,y,items):
    for item in items:
        if x == item["x"] and y == item["y"]:
            return True
    return False

def print_map(size_x,size_y,pusher_x,pusher_y,boxes):
    for y in range(size_y):
        for x in range(size_x):
            if x == pusher_x and y == pusher_y:
                print(" P ", end="")
            elif check_overlap(x,y,boxes):
                print(" B ", end="")
            elif check_overlap(x,y,destination):
                print(" D ", end="")
            else:
                print(" - ", end="")
        print()

def input_process(direction):
    dx = 0
    dy = 0
    if direction == "W":
        dy -= 1
    elif direction == "A":
        dx -= 1
    elif direction == "S":
        dy += 1
    elif direction == "D":
        dx += 1
    else:
        print("You enter wrong button please this again")
    return dx, dy

def in_map(x, y, size_x, size_y):
    return 0 <= x <= size_x and 0 <= y <= size_y

while True:
    print_map(size_x,size_y,pusher_x,pusher_y,boxes)
    direction = input("What is your next move? W/A/S/D: ").upper()
    dx, dy = input_process(direction)
    if box1["x"] == pusher_x + dx and box1["y"] == pusher_y + dy:
        if in_map(box1["x"] + dx, box1["y"] + dy, size_x, size_y):
            if box1["x"] + dx != box2["x"] != box3["x"] or box1["y"] + dy != box2["y"] !=  box3["y"]:
                box1["x"] += dx
                box1["y"] += dy
                pusher_x += dx
                pusher_y += dy
        else:
            print("Nope!")
    elif box2["x"] == pusher_x + dx and box2["y"] == pusher_y + dy:
        if in_map(box2["x"] + dx, box2["y"] + dy, size_x, size_y):
            if box2["x"] + dx != box1["x"] != box3["x"] or box2["y"] + dy != box1["y"] !=  box3["y"]:
                box2["x"] += dx
                box2["y"] += dy
                pusher_x += dx
                pusher_y += dy
        else:
            print("Nope!")
    elif box3["x"] == pusher_x + dx and box3["y"] == pusher_y + dy:
        if in_map(box3["x"] + dx, box3["y"] + dy, size_x, size_y):
            if box3["x"] + dx != box1["x"] != box2["x"] or box3["y"] + dy != box1["y"] !=  box2["y"]:
                box3["x"] += dx
                box3["y"] += dy
                pusher_x += dx
                pusher_y += dy
        else:
            print("Nope!")
    elif [box1["x"], box1["y"]] == [dest1["x"], dest1["y"]] and [box2["x"], box2["y"]] == [dest2["x"], dest2["y"]] and [box3["x"], box3["y"]] == [dest3["x"], dest3["y"]]:
        print("You win")
        break
    else:
        next_pusher_x = pusher_x + dx
        next_pusher_y = pusher_y + dy
        if in_map(next_pusher_x,next_pusher_y,size_x,size_y):
            pusher_x = next_pusher_x
            pusher_y = next_pusher_y
