def solution():
    n=2520
    while True:
        for j in (n%i for i in range(1, 21)):
            if j != 0:
                break
        else:
            print 'Answer: %s' % n
            break
        n+=20

if __name__ == '__main__':
    solution()