def staircase(n):
    # Write your code here
    for_hash = range(0,n)
    for_space = range(n, 0, -1)
    for i, j in zip(for_space, for_hash):
        print("{}{}".format(' '*i, '#'*j))

staircase(6)