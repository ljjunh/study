s = input()
res = ""
for i in s:
    if 97 <= ord(i) <= 122:
        if (ord(i)+13) > 122:
            res += chr(ord(i) - 13)
        else:
            res += chr(ord(i) + 13)
    elif 65 <= ord(i) <= 90:
        if (ord(i)+13) > 90:
            res += chr(ord(i) - 13)
        else:
            res += chr(ord(i) + 13)
    else:
        res += i
print(res)