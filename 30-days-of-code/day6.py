# https://www.hackerrank.com/challenges/30-review-loop/problem

# Enter your code here. Read input from STDIN. Print output to STDOUT

n = int(input())
strings = []

while n > 0:
    strings.append(input())
    n = n - 1

for s in strings:
    even = []
    odd = []
    for i in range(len(s)):
        if i % 2 == 0:
            even.append(s[i])
        else:
            odd.append(s[i])
    print('{0} {1}'.format(''.join(even), ''.join(odd)))
