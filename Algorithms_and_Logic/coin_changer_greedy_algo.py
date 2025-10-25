# FILE: coin_changer_greedy_algo.py
# CONCEPT: Greedy Algorithm and Control Flow
# DEMONSTRATES: The "greedy" approach to finding the fewest coins for a given amount, 
#               by repeatedly subtracting the largest possible denomination (using while loops).

def select_coins():
    # Denomination counters
    two_pounds = 0  # 200p
    one_pound = 0   # 100p
    fifty_pence = 0 # 50p
    twenty_pence = 0 # 20p
    ten_pence = 0   # 10p
    five_pence = 0  # 5p
    two_pence = 0   # 2p
    one_penny = 0   # 1p
    
    money_in_pence = int(input("The amount of money in pence is: "))
    remaining_pence = money_in_pence
    
    # Use successive subtraction for the greedy approach
    
    while(remaining_pence >= 200):
        remaining_pence -= 200
        two_pounds += 1
    
    while(remaining_pence >= 100):
        remaining_pence -= 100
        one_pound += 1
    
    while(remaining_pence >= 50):
        remaining_pence -= 50
        fifty_pence += 1
        
    while(remaining_pence >= 20):
        remaining_pence -= 20
        twenty_pence += 1
        
    while(remaining_pence >= 10):
        remaining_pence -= 10
        ten_pence += 1
        
    while(remaining_pence >= 5):
        remaining_pence -= 5
        five_pence += 1
        
    while(remaining_pence >= 2):
        remaining_pence -= 2
        two_pence += 1
        
    if(remaining_pence >= 1):
        one_penny += 1
    
    print(f"Change for {money_in_pence} pence:")
    print("Two pounds:", two_pounds)
    print("One pound:", one_pound)
    print("Fifty pence:", fifty_pence)
    print("Twenty pence:", twenty_pence)
    print("Ten pence:", ten_pence)
    print("Five pence:", five_pence)
    print("Two pence:", two_pence)
    print("One penny:", one_penny)
