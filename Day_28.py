n = int(input())
name = []
mail = []
names = []
for _ in range(n):
    inp = input().split()
    name.append(inp[0])
    mail.append(inp[1])
for mai in mail:
    if "@gmail" in mai:
        a = mail.index(mai)
        names.append(name[a])
names.sort()
for nam in names:
    print(nam)        
