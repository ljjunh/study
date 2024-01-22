# 2차원배열 풀이
# arr = []
# num_max = -1
# index1 = -1
# index2 = -1
# for _ in range(9):
#     arr.append(list(map(int, input().split())))
# for idx1, i in enumerate(arr):
#     for idx2, j in enumerate(i):
#         if num_max < j:
#             num_max = j
#             index1 = idx1
#             index2 = idx2
# print(num_max)
# print(index1 + 1, index2 + 1)

# 1차원배열 풀이
import sys
arr = []
for i in range(9):
    arr += list(map(int, sys.stdin.readline().split())) #1차원리스트로 arr에 입력값 계속 추가
max_num = max(arr) #최댓값
max_num_idx = arr.index(max_num) 

print(max_num)
print(max_num_idx // 9 + 1, max_num_idx % 9 + 1)
# 최댓값의 인덱스를 구하면 42이고, 문제에서는 9x9배열이니까 
# 42 // 9의 값은 행이 될거고
# 42 % 9의 값은 열이 됨
# 문제에서 인덱스가 아닌 몇번째 줄인지 물어봤으니 +1씩