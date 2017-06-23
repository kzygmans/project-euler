def solution():
    file = open('files/p022_names.txt', 'r')
    names = file.read()
    file.close()

    names = names.split(",")
    for i, e in enumerate(names):
        names[i] = e.replace('"','')
    names = sorted(names)

    sum = 0
    for i, e in enumerate(names):
        temp = 0
        for l in e:
            temp += (ord(l) - 64)
        sum += (temp * (i+1))

    print 'Answer: %i' % sum

if __name__ == '__main__':
    solution()