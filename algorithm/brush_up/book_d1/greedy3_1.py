money = 1260
coins = [500, 100, 50, 10]
count = 0
for i in coins:
    count += money // i 
    money = money % i
print(count)