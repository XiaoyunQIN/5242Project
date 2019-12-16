def mySqrt(x):
    left = 0
    right = x
    while right - left > 1:
        
        mid = (left + right) // 2
        print(mid*mid)
        if mid*mid == x:
            return mid
        elif mid*mid > x:
            right = mid-1
        else:
            left = mid
    if right*right <= x:
        return right
    else:
        return left
print(mySqrt(9))



