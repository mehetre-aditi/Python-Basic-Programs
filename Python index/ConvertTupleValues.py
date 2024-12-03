def convert_fun(t):
    result=tuple((int(x[0]),int(x[1]))for x in t)
    return result
t=(('333','33'),('1234','45'))
print("Original tuple values:")
print(t)
print("new tuple values:")
print(convert_fun(t))