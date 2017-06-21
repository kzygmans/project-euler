from datetime import date


def solution():
    sum = 0
    for y in range(1901, 2001):
        for m in range(1, 13):
            if(date(y, m, 1).weekday()==6):
                sum += 1

    print 'Answer: %i' % sum

if __name__ == '__main__':
    solution()