#accumulating distinct values
def accumDist():
    myList = [1,4,5,6,6,7,8]
    dv = []
    for v in myList:
        print(v)
        i = 0
        dv.append(v)
        while dv[i] != v:
            i += 1
        if i != len(dv):
            del(dv[-1])
        print(dv)
    return dv
        

