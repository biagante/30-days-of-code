# Enter your code here. Read input from STDIN. Print output to STDOUT

x = int(input())

mapp = {}

for i in range(x):
    text = input().split()
    mapp[text[0]] = text[1]

while True:
    try:
        inpt = input()
        if inpt in mapp:
            print(inpt+"="+mapp[inpt])
        else:
            print("Not found")
    except EOFError:
        break
