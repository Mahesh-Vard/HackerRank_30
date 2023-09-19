string = input()
try:
    string = int(string)
    print(string)
except ValueError:
    print("Bad String")    
