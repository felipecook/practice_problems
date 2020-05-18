# Given an int n, return True if it is within 10 of 100 or 200.
# Note: abs(num) computes the absolute value of a number.

# near_hundred(93) → True
# near_hundred(90) → True
# near_hundred(89) → False
def near_hundred(n):
    if (89 < n < 111) or (189 < n < 211):
        return True
    else:
        return False


print(near_hundred(200))
print(near_hundred(1))
print(near_hundred(-3))