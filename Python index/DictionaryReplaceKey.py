dict={'Mon':1,'Tue':2,'Wed':3,'Thu':4}
print("The given dictionary : ",dict)

check_key=input("Enter key to check : ")
check_value=input("Enter value : ")

if check_key in dict:
    print("key is present")
    dict[check_key]=check_value
else:
    print("key is not present")
    dict[check_key]=check_value
print("update dictionary: ",dict)
