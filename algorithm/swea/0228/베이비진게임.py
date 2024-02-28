T = int(input())
for tc in range(1, T + 1):
    temp = list(map(int, input().split()))
    player_1 = []
    player_2 = []
    for i in range(len(temp)):
        if i % 2 == 0:
            player_1.append(temp[i])
        else:
            player_2.append(temp[i])

    arr1 = player_1[:2]
    arr2 = player_2[:2]
    cnt = 0
    visited1 = [0] * 10
    visited1[player_1[0]] += 1
    visited1[player_1[1]] += 1
    visited2 = [False] * 10
    visited2[player_2[0]] += 1
    visited2[player_2[1]] += 1
    
    for i in range(2, len(player_1)):
        arr1.append(player_1[i])
        arr2.append(player_2[i])
        visited1[player_1[i]] += 1
        visited2[player_2[i]] += 1
        if 3 in visited1:
            print(f"#{tc} 1")
            break
        if 3 in visited2:
            print(f"#{tc} 2")
            break
        
        for j in range(8):
            if visited1[j] and visited1[j+1] and visited1[j+2]:
                print(f"#{tc} 1")
                exit()
             
            if visited2[j] and visited2[j+1] and visited2[j+2]:
                print(f"#{tc} 2")
                exit()
    else:
        print(f"#{tc} 0")
        
