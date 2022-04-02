List1 = [1, 3, 4, 5]
List2 = [0, 7, 6, 5]

for x in List1:
    for y in List2:
        if x > y:
            print(x, " From List1 is greater then List2", y)
        elif x == y:
            print(x, "equal", y)
        else:
            print(x, " From List 1 is less then List2", y)