import sys
input = sys.stdin.readline

def recur(n, s, lst):
    if n == L:
        cnt = 0
        cnt2 = 0
        for k in lst:
            if k in "aeiou":
                cnt += 1
            else:
                cnt2 += 1
        if cnt >= 1 and cnt2 >=2:
            print(*lst, sep="")
        return
    for i in range(s, C):
        if visited[i]:
            continue
        visited[i] = 1
        recur(n+1, i+1, lst+[arr[i]])
        visited[i] = 0
    
L, C = map(int, input().split())
arr = list(input().split())
arr.sort()
visited = [0] * (C)
recur(0, 0, [])