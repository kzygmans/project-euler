import itertools


def solution():
    permutations = list(itertools.permutations(['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']))
    result = ''.join(permutations[999999])
    print 'Answer: %s' % result

if __name__ == '__main__':
    solution()