
def find_fewest_coins(coins, amount):

    if amount < 0:
        raise ValueError("target can't be negative")

    dp = [None] * (amount + 1)

    dp[0] = []

    for value in range(1, amount + 1):
        print(f"the value of value {value}")
        
        for coin in coins:
            print(f"the coin {coin}")
            if coin <= value and dp[value - coin] is not None:
                print(f"dp[]  = {dp[value - coin]}")
                candidate = dp[value - coin] + [coin]
                print(f"cadidate {candidate}")
                if dp[value] is None or len(candidate) < len(dp[value]):
                    print("Entra aqui")
                    dp[value] = candidate

    if dp[amount] is None:
        raise ValueError("can't make target with given coins")

    return sorted(dp[amount])

print(find_fewest_coins([1, 5, 10, 21, 25], 63))