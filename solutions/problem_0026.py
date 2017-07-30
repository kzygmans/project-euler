def cycle(n):
    mod = 10 % n
    count = 0

    while(mod != 1 and count < n):
        mod *= 10
        mod = mod % n
        count += 1

    return count

def solution():
    result = 0
    longest_cycle = 0

    for i in range(1, 1001):
        if(i % 2 == 0 or i % 5 == 0):
            continue
        tmp = cycle(i)
        if(tmp > longest_cycle):
            result = i
            longest_cycle = tmp

    print 'Answer: %i' % result

if __name__ == '__main__':
    solution()
