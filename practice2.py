def calcPloy(n):
    if n==0 or n==1:
        return 1
    else:
        return calcPloy(n-1)+calcPloy(n-2)

print(calcPloy(5))

