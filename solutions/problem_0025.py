def solution():
    a = 1
    b = 1
    i = 3
    while True:
        fib = a + b
        a, b = b, fib
        if (len(str(fib)) == 1000):
            break
        i += 1

    print 'Answer: %i' % i

if __name__ == '__main__':
    solution()