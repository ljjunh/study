import sys
input = sys.stdin.readline
n = int(input())
stack = []
operator = []
temp = 0
cnt = 1
for i in range(n):
    num = int(input())
    while cnt <= num: # i까지 stack에 push
        stack.append(cnt)
        operator.append("+")
        cnt += 1
    if stack[-1] == num: # stack의 top이 i와 같으면 pop
        stack.pop()
        operator.append("-")
    else:
        print("NO") # stack의 top이 i와 다르면 스택을 만들 수 없음
        temp = 1 # 1,2,3,4처럼 오름차순으로 스택이 입력되는데
        break    # top > num이면 num은 top보다 더 아래 있기 때문
if temp == 0:
    for i in operator:
        print(i)
