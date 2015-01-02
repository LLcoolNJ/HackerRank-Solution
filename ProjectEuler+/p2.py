def fib():
    x,y = 0,1
    while True:
        yield x
        x,y = y, x+y
def even(seq):
    for number in seq:
        if not number % 2:
            yield number
def sumofev(seq,k):
    for number in seq:
        if number > k:
            break
        yield number
for i in range(input()):
    print sum(even(sumofev(fib(),input())))