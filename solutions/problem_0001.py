def solution1():
    sum = 0
    for i in range(1, 1000):
        if(i % 3 == 0 or i % 5 == 0):
            sum += i
    print 'Answer: %s' % sum

def solution2():
    sum = 0
    for i in range(3, 1000, 3):
        sum += i
    for i in range(5, 1000, 5):
        if(i % 3 != 0):
            sum += i
    print 'Answer: %s' % sum

if __name__ == '__main__':
    solution1()