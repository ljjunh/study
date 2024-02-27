path = []
visited = [False] * 7
def KFC(x):
    if x == 3:
        print(path)
        return
    for i in range(1, 7):
        if not visited[i]:
            visited[i] = True
            path.append(i)
            KFC(x + 1)
            path.pop()
            visited[i] = False
KFC(0)

path2 = []
def KFC2(x):
    if x == 5: 
        print(path2)
        return
    for i in range(1, 5):
        path2.append(i)
        KFC2(x + 1)
        path2.pop()
#KFC2(0)