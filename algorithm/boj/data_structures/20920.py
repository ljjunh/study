import sys
input = sys.stdin.readline
n, m = map(int, input().split())
arr = {}
for _ in range(n):
    temp = input().rstrip()
    if len(temp) < m:
        continue
    else:
        if temp in arr: # 만약 딕셔너리에 해당 key가 있다면
            arr[temp] += 1 # 값 증가
        else: # 딕셔너리에 해당 key가 없다면
            arr[temp] = 1 # 초기화
res = sorted(arr.items(), key = lambda x : (-x[1], -len(x[0]), x[0])) #value 내림차순, key길이 내림차순, key오름차순(a,b,c,...)
for i in res:
    print(i[0]) #튜플의 idx0번들만 출력