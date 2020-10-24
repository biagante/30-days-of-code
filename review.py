# Enter your code here. Read input from STDIN. Print output to STDOUT

t = int(input())
for _ in range(t):
    str = input()
    first = ""
    second = ""

    for i, c in enumerate(str):
        if(i & 1) == 0:
            first += c
        else:
            second += c
            
    print(first, second)
