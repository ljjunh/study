T = int(input())
N = 0
arr = []
# 투포인터
def get_result():
    a = 0
    b = (len(arr) + 1) // 2

    for turn in range(len(arr)):
        if turn % 2 == 0:
            print(arr[a], end = " ")
            a += 1
        else:
            print(arr[b], end = " ")
            b += 1
for tc in range(1, T + 1):
    N = int(input())
    arr = list(map(str, input().split()))
    print(f"#{tc}", end = " ")
    get_result()
    print()


# 내코드
# T = int(input())
# for tc in range(1, T + 1):
#     N = int(input())
#     arr = list(input().split())
#     a = 0
#     if N % 2 == 0:
#         b = N // 2
#         t = N // 2
#     else:
#         b = N // 2 + 1
#         t = N // 2 + 1
#     print(f"#{tc}", end = " ")
#     for _ in range(t):
#         if a < N:
#             print(arr[a], end = " ")
#             a += 1
#         if b < N:
#             print(arr[b], end = " ")
#             b += 1
#     print()
        
