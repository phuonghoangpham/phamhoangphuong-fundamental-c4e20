for i in range(1,10):
    #draw 1 line
    s=' '
    for j in range(1,10):
        s += '{:2} '.format(i * j)
    print(s)