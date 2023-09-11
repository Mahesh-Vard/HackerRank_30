# n = int(input())
# lis = []
# for _ in range(0, n):
#     Number = input().split()
#     lis = lis+Number
# for i in range(0, n):
#     inp = input()
#     if inp in lis:
#         number_index = lis.index(inp)+1
#         print(f"{inp}={lis[number_index]}")
#     else:
#         print("Not found")
x = int(input())

dictt = {}

for i in range(x):
    text = input().split()
    dictt[text[0]] = text[1]

while True:
    try:
        inpt = input()
        if inpt in dictt:
            print(inpt+"="+dictt[inpt])
        else:
            print("Not found")
    except EOFError:
        break
