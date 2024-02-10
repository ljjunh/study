while True:
    n = int(input())
    if n == 0:
        break
    arr = [True for _ in range(n+1)] #0~7까지의 true배열
    for i in range(2, int(n**0.5)+1):
        j = 2
        while i * j <= n:
            arr[i*j] = False
            j += 1
    res = 0
    for i in range(2, n):
        if arr[i] == True:
            temp = i
        else:
            continue
        for j in range(n-1, 1, -1): # j = 7, 6, 5, 4, 3, 2
            if arr[j] == True:
                if i + j == n:
                    if j-temp > res:
                        res = j-temp
                        print(f"{n} = {temp} + {j}")
                        break
    if res == 0:
        print('"Goldbach\'s conjecture is wrong."')

        
            
        

        
    
    

