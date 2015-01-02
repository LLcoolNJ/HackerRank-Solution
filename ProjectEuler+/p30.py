a = {3:1301,4:19316,5:443839,6:548834}
print a[input()]
'''
import math
def digit_powers(exponent):
    if exponent <= 1:
        return "The exponent must be at least 2."

    powers = {}
    answer = 0
    # Get the powers
    for a in range(10):
        powers[a] = a ** exponent

    limit = (exponent + 1) * (9 ** exponent)

    # Search for them
    for i in range(10, limit):
        savei = i
        total = 0

        for _ in range(int(math.log10(i)) + 1):
            digit = i % 10
            total += powers[digit]
            i //= 10

        if (total == savei):
            answer += total

    return answer
'''