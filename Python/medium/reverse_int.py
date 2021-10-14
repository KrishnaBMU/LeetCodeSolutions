def reverseInt(n):
    result = 0
    while(n > 0):
        a = n % 10
        result = (result * 10) + a
        n = n // 10
    return result


n = int(input())
if(n > 0):
    print(reverseInt(n))
else:
    n = n*(-1)
    print((-1)*(reverseInt(n)))

