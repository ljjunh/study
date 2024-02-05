# 슬라이싱 사용
# T = int(input())
# for i in range(T):
#     arr = list(input().split())
#     for i in arr:
#         print(i[::-1], end = " ")

# 스택 사용
T = int(input())
for i in range(T):
    string = input()
    string += " " # 마지막꺼까지 출력하기 위해서 문자열 뒤에 공백 추가
    stack = []
    for j in string: 
        if j != " ": # 공백이 나올때까지 stack에 추가
            stack.append(j) 
        else:
            while stack: # 공백이 나오면 stack에 있는거 전부 출력
                print(stack.pop(), end = "")
            print(end = " ")
    print()