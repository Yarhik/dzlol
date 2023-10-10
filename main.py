def minimum_coins(target_amount, coin_values):
    coin_values.sort(reverse=True)

    coin_count = [0] * len(coin_values)
    total_coins = 0

    for i in range(len(coin_values)):
        coin_count[i] = target_amount // coin_values[i]
        target_amount -= coin_count[i] * coin_values[i]
        total_coins += coin_count[i]

    return total_coins, coin_count

target_amount = 48
coin_values = [7, 3]

total_coins, coin_count = minimum_coins(target_amount, coin_values)

print(f"Мінімальна кількість монет: {total_coins}")
print("Кількість монет кожного номіналу:")
for i in range(len(coin_values)):
    print(f"{coin_values[i]} валют: {coin_count[i]}")
