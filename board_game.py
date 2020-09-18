def drawboard(x):
    x = int(x)

    i = 0
    hor = "---"
    ver = "|"
    hor = hor*x
    ver = ver*x
    while i < x+1:
        print(hor)
        if not (i == x):
            print(ver)
        i +=1
print(drawboard(3))