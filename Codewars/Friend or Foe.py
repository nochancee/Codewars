def friend(x):
    x1 = []
    for i in x: 
        if len(i) == 4:
            x1.append(i)
    return(x1)

def friend(x):
    return [f for f in x if len(f) == 4]    