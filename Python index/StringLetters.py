def string_test(s):
    d={"upper":0,"lower":0}
    for c in s:
        if c.isupper():
            d["upper"]+=1
        if c.islower():
            d["lower"]+=1
    print("Original String : ",s)
    print("Number of uppercase characters : ",d["upper"])
    print("Number of lowercase cgaracters : ",d["lower"])
string_test("The quick Brown Fox")