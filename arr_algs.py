arr=[10,2,5,2,5,2,2,2,2]
def FindMin(ar):
    armin=ar[0]
    for i in ar:
        if i < armin:
            armin = i
    return armin
def FindMean(ar):
    sum=0.0
    for i in ar:
        sum=sum + i
    return sum/len(ar)
print (FindMin(arr))
print (FindMean(arr))