import random
D12 = range (1, 12)
roll = input("Type 'roll' to roll the dice: " )
if roll == "roll":
    print(random.choice(D12))