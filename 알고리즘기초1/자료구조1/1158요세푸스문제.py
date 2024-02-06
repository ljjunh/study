# from collections import deque
# n, m = map(int, input().split())
# arr = deque(list(range(1, n+1)))
# res = []
# cnt = 0
# while len(res) < n:
#     cnt += 1
#     if cnt % m == 0:
#         res.append(arr.popleft())
#     else:
#         arr.append(arr.popleft())

# print(str(res).replace("[", "<").replace("]",">"))

# from collections import deque
# n, k = map(int, input().split())
# arr = deque(list(range(1, n+1)))
# res = []
# while arr:
#     for _ in range(k-1):
#         arr.append(arr.popleft())
#     res.append(arr.popleft())
# print(str(res).replace("[", "<").replace("]",">"))

n, k = map(int, input().split())
arr = [i for i in range(1, n+1)] # 맨 처음 원에 앉아있는 사람들

res = [] # 제거된 사람들
num = 0 # 제거될 사람의 인덱스 번호

for i in range(n):
    num += k - 1
    if num >= len(arr):
        num = num % len(arr)
    res.append(str(arr.pop(num)))
print("<", ", ".join(res), ">", sep = "")