T = int(input())
for tc in range(1, T + 1):
    dict = {}
    arr1 = input()
    arr2 = input()
    for i in arr1:
        dict[i] = 0
    for i in arr2:
        if dict.get(i) != None:
            dict[i] += 1
    max_value = 0
    for key, value in dict.items():
        if value > max_value:
            max_value = value
    print(f"#{tc} {max_value}")