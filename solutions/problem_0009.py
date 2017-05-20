def solution():
    a = 1
    found = False

    while(not found):
        for b in range(a+1, 1000-a):
            c = 1000 - a - b
            if(a**2 + b**2 == c**2):
                print 'Answer: %i' % (a*b*c)
                found = True
                break
        a += 1

if __name__ == '__main__':
    solution()