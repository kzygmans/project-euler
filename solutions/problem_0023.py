def solution():
    abundant_numbers = []
    for i in range(1, 28123):
        tmp_sum = 0
        for j in range(1, (i/2)+1):
            if (i % j == 0):
                tmp_sum += j
        if (tmp_sum > i):
            abundant_numbers.append(i)

    abundant_sums = set()
    for i in abundant_numbers:
        for j in abundant_numbers:
            tmp_sum = i+j
            if (tmp_sum < 28123):
                abundant_sums.add(tmp_sum)

    non_abundant = list(set([i for i in range(1, 28123)]) - abundant_sums)
    print 'Answer: %i' % sum(non_abundant)

if __name__ == '__main__':
    solution()