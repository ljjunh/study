N = int(input())
drink = list(map(int, input().split()))
result = (sum(drink) - max(drink)) / 2 + max(drink)
print('%g'%result) # 정수면 정수, 실수면 실수로 출력