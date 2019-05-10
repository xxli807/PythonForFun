def msg():
    msg="hello world"
    print(msg)
    last_name="smith"
    for letter in last_name:
        print(letter, " ") # note a space between
    x = 3
    print("x is " + ("great that 3" if x < 3 else "small than 3"))
    if x > 0 and x < 2:
        x = 3
        print(x)
    else:
        raise ValueError("x is great than 2", x)
    
# msg(123) 

def reverse(x):
    strX = str(x)
    length = len(strX)
    if length == 1:
        return x
    else:
        firstChar = strX[0]
        subStrx = strX[1:length]
        if firstChar == "-":
            return "-".join(subStrx[::-1])
        elif firstChar == "1":
            yyy = subStrx[::-1] 
            return subStrx[::-1] 
        else:
            xxx = strX[::-1]
            return strX[::-1]

reverse(123)
