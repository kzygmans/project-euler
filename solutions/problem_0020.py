def solution():
    factorial = 1
    sum = 0

    for i in range(1, 101):
        factorial *= i

    for i in str(factorial):
        sum += int(i)

    print 'Answer: %i' % sum

if __name__ == '__main__':
    solution()