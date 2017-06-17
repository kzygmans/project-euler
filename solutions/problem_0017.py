def solution():
    units = [0, len('one'), len('two'), len('three'), len('four'),
             len('five'), len('six'), len('seven'), len('eight'), len('nine')]
    tens = [len('ten'), len('eleven'), len('twelve'), len('thirteen'),
            len('fourteen'), len('fifteen'), len('sixteen'), len('seventeen'),
            len('eighteen'), len('nineteen')]
    tens2 = [0, 0, len('twenty'), len('thirty'), len('forty'), len('fifty'),
             len('sixty'), len('seventy'), len('eighty'), len('ninety')]
    hundred = 7
    thousand = 8

    sum = 0
    for i in range(1, 1001):
        th = i / 1000
        h = (i - th * 1000)/100
        te = i - (h * 100 + th * 1000)
        #print '%s, %s, %s, %s' % (i, te, h, th)
        if(th > 0):
            sum += (thousand + units[th])
        if(h > 0):
            sum += (hundred + units[h])
            if(te != 0):
                # add length of 'and'
                sum += 3
        if(te >= 20):
            print '%i, %i, %i' % (i, te/10, te%10)
            sum += (tens2[te / 10] + units[te % 10])
        elif(te >= 10):
            sum += tens[te % 10]
        elif(te > 0):
            sum += units[te]

    print 'Answer: %i' % sum

if __name__ == '__main__':
    solution()