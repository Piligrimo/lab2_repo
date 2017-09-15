str="Hello, world!"
def Inverse(st):
    inv=""
    for i in range(len(st)):
        inv=inv+str[len(st)-i-1]
    return inv
print (Inverse(str))
