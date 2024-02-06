T = int(input())
for tc in range(1, T + 1):
    text, pattern = input().split()
    lt = 0
    rt = len(pattern)
    cnt = 0
    while rt <= len(text):
        if text[lt:rt] == pattern:
            lt += len(pattern)
            rt += len(pattern)
            cnt += 1
        else:
            lt += 1
            rt += 1
    print(f"#{tc} {len(text) - (len(pattern) * cnt) + cnt}")

# T = int(input())
# for tc in range(1, T + 1):
#     text, pattern = input().split()
#     temp = text.count(pattern)
#     print(f"#{tc} {len(text) - (len(pattern) * temp) + temp}")