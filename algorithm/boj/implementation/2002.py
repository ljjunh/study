import sys
input = sys.stdin.readline
n = int(input())
arr1 = []
for i in range(n):
    arr1.append(input().rstrip())

arr2 = []
for j in range(n):
    arr2.append(input().rstrip())

start = 0
end = 0
cnt  = 0
for i in range(n):
    if arr1[start] == arr2[end]:
        start += 1
        end += 1
    elif arr1[start] != arr2[end]:
        arr1.remove(arr2[end])
        cnt += 1
        end += 1
        
print(cnt) 
    