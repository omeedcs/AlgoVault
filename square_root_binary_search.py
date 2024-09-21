def sqrt(x):
    if x < 2:
        return x
    # we are looking within the bounds of x.
    left = 0 
    right = x
    while left <= right:
        mid = (left) + (right - left) // 2
        val = mid * mid
        if val < x:
            left += 1
        elif val > x:
            right -= 1
        else:
            return mid
    return right

print(sqrt(25))
print(sqrt(100))
print(sqrt(36)) 
