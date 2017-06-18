triangle = """75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23"""


def solution():
    numbers_list = []
    for line in triangle.splitlines():
        numbers_list.append(line)

    for lId, l in enumerate(numbers_list):
        numbers_list[lId] = l.split(' ')
        for eId, e in enumerate(numbers_list[lId]):
            numbers_list[lId][eId] = int(e)

    numbers_list = numbers_list[::-1]

    for iId, i in enumerate(numbers_list):
        for jId, j in enumerate(i):
            if(j > i[jId+1]):
                numbers_list[iId+1][jId] += j
            else:
                numbers_list[iId+1][jId] += i[jId+1]
            if(jId == len(i)-2):
                break
        if(iId == len(numbers_list)-2):
            break

    print 'Answer: %i' % list(reversed(numbers_list))[0][0]

if __name__ == '__main__':
    solution()