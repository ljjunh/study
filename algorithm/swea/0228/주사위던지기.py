arr = [1, 2, 3, 4, 5, 6]
N = 3
path = [] # 흔적

def func(lev, start):
    if lev == N:
        print(path)
        return
    
    for i in range(start, 7):
        path.append(i)
        func(lev + 1, i) # i+1이 아니라 i인 이유 : 주사위는 1 2 3 순서대로 있는게 아니라 1 1 1이 될수도있어서
        # i+1(2)부터 진입하는게 아니라 i(1) 부터 진입
        path.pop()

func(0, 1)