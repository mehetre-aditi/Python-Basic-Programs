num=int(input("Enter any positive number : "))
try:
    if num>0:
        raise ValueError("Input number is correct(positive number)")
    else:
        raise ValueError("Input number is incorrect(negative number)")
except ValueError as e:
    print(e)