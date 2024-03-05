import sys
while True:
    s = sys.stdin.readline().rstrip("\n")
    if not s:
        break
    string = s
    lowwer = 0
    upper = 0
    num = 0
    space = 0
    for i in string:
        if i == " ":
            space+=1
        elif 97 <= ord(i) <= 122:
            lowwer += 1
        elif 65 <= ord(i) <= 90:
            upper += 1
        else:
            num += 1
    print(lowwer, upper, num, space)