def plusMinus(arr):
    # Write your code here
    lenth = len(arr)
    positive_num = len([num for num in arr if num > 0])
    negetive_num = len([num for num in arr if num < 0])
    zero_num = len([num for num in arr if num == 0])
    print("{:.6f}".format(positive_num/lenth))
    print("{:.6f}".format(negetive_num/lenth))
    print("{:.6f}".format(zero_num/lenth))

plusMinus([-4,3,-9,0,4,1])