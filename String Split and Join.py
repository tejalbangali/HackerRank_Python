#Link --> https://www.hackerrank.com/challenges/python-string-split-and-join/problem


def split_and_join(line):
    line=line.split(' ')
    line='-'.join(line)
    return line
    
line = input()
result = split_and_join(line)
print(result)
