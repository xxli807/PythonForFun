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
    
msg() 