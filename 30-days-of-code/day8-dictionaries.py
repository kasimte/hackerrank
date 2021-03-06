# https://www.hackerrank.com/challenges/30-dictionaries-and-maps/problem

# Enter your code here. Read input from STDIN. Print output to STDOUT

n = int(input())
book = {}

for x in range(0,n):
    line = input().split()
    book[line[0]] = line[1]

while True:
    try:
        line = input().split()
        name = line[0]
        if name in book:
            entry = book[name]
            print("{0}={1}".format(name, entry))
        else:
            print("Not found")
    except EOFError:
        break
