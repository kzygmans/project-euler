def solution():
    number = 2 ** 1000
    sum = 0

    for i in str(number):
        sum += int(i)

    print 'Answer: %i' % sum

if __name__ == '__main__':
    solution()