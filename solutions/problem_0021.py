def solution():
    amicable_numbers_list = []

    for i in range(1, 10001):
        if (i in amicable_numbers_list):
            continue
        sum1 = 0
        sum2 = 0
        for j in range(1, (i / 2) + 1):
            if (i % j == 0):
                sum1 += j
        for j in range(1, (sum1 / 2) + 1):
            if (sum1 % j == 0):
                sum2 += j
        if (i == sum2 and i != sum1):
            amicable_numbers_list.append(i)
            amicable_numbers_list.append(sum1)

    print 'Answer: %i' % sum(amicable_numbers_list)

if __name__ == '__main__':
    solution()