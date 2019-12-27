# https://www.hackerrank.com/challenges/python-lists/problem

if __name__ == '__main__':
    N = int(input())
    array = [] # could also be list()

    while N > 0:
        temp = input().split()
        command = temp[0]
        args = temp[1:]
        if command == "print":
            print(array)
        else:
            eval("array.{0}{1}".format(command,tuple(map(int,args))))
        N = N - 1
