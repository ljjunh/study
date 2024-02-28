T = int(input())

def run2(arr):
    for i in range(1, 9):
        if arr[i-1] > 0 and arr[i] > 0 and arr[i+1] > 0:
            return 1
        
for tc in range(1, T + 1):
    temp = list(map(int, input().split()))
    player_1 = [0] * 10
    player_2 = [0] * 10
    ans = 0
    for i in range(len(temp)):
        if i % 2 == 0:
            player_1[temp[i]] += 1
            if 3 in player_1:
                ans = 1
                break
            if run2(player_1) == 1:
                ans = 1
                break
        else:
            player_2[temp[i]] += 1
            if 3 in player_2:
                ans = 2
                break
            if run2(player_2) == 1:
                ans = 2
                break
    print(f"#{tc} {ans}")
    
            



        
