prices = list(map(int, input().split()))
n = len(prices)
wait_days = []

for i in range(n):
    max_price = 0
    for j in range(i+1, n):
        if prices[j] > prices[i]:
            max_price = max(max_price, prices[j])
            break
    wait_days.append(str(0 if max_price == 0 else j-i))

print(" ".join(wait_days), end="")