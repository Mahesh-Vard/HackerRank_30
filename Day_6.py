n = int(input())
for _ in range(n):
    User_inp = input()
    inp_list = []
    for letter in User_inp:
        inp_list.append(letter)
    for i in range(0, len(User_inp), 2):
        print(inp_list[i], end="")
    print(end=" ")
    for i in range(1, len(User_inp), 2):
        print(inp_list[i], end="")
    print()    
