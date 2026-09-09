import random

# generate winning number list
winning_number_list = random.sample(range(1, 69), 5)
winning_number_list.sort()
winning_number_list.append(f"powerball:{random.randint(1, 26)}")

# convert winning number list to string
winning_number = ",".join(str(num) for num in winning_number_list)


buyer_number_list = []
buyer_amount = 100000000

# generate buyer number list
for i in range(buyer_amount):
    buyer_number = random.sample(range(1, 69), 5)
    buyer_number.sort()
    buyer_number.append(f"powerball:{random.randint(1, 26)}")
    buyer_number = ",".join(str(num) for num in buyer_number)
    
    buyer_number_list.append(buyer_number)
    


print(f"Today's winning number is {winning_number}:")
has_winner = False
for buyer_number in buyer_number_list:
    if buyer_number == winning_number:
        print("we have a winner!")
        print(f"the buyer number is {buyer_number}")
        has_winner = True
        break

if not has_winner:
    print(f"the winning number is {winning_number}")
    print("we have no winner!")
    