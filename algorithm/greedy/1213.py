import collections
word = input()
check_word = collections.Counter(word)
center = ""
cnt = 0
result = ""
for key, value in list(check_word.items()):
    if value % 2 != 0:
        cnt += 1
        center = key
        if cnt > 1:
            print("I'm Sorry Hansoo")
            exit()

for k, v in sorted(check_word.items()):
    result += k * (v//2)
print(result + center + result[::-1])
