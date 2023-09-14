def coins(count_of_coins):

    coins_array = []

    while len(coins_array) < int(count_of_coins):
        try:
            n_coins = int(input("Enter 1 (heads) or 0 (tails): "))
        except ValueError:
            print("Invalid input. Please enter an integer.")
            continue
        
        if n_coins != 0 and n_coins != 1:
            print("No, only 0 or 1.")
            continue
        
        coins_array.append(n_coins)
    
    return coins_array



def result (coins_array: list[int]):
    count0 = 0
    count1 = 0
    for i in coins_array:
        if i == 0: count0 += 1
        else: count1 += 1
    
    if count0 < count1: return count0 
    elif count0 > count1: return count1
    else: return "Without a difference."


count_of_coins = input("Enter the count of coins: ")
array_coins = coins(count_of_coins)

print(f"Result: {result(array_coins)}")
