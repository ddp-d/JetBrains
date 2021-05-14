user_money = int(input())

if user_money in range(23, 678):
    count_chicken = user_money // 23
    if count_chicken > 1:
        print(f"{count_chicken} chickens")
    else:
        print(f"{count_chicken} chicken")
elif user_money in range(678, 1296):
    count_goat = user_money // 678
    if count_goat > 1:
        print(f"{count_goat} goats")
    else:
        print(f"{count_goat} goat")
elif user_money in range(1296, 3848):
    count_pig = user_money // 1296
    if count_pig > 1:
        print(f"{count_pig} pigs")
    else:
        print(f"{count_pig} pig")
elif user_money in range(3848, 6769):
    count_cow = user_money // 3848
    if count_cow > 1:
        print(f"{count_cow} cows")
    else:
        print(f"{count_cow} cow")
elif user_money >= 6769:
    count_sheep = user_money // 6769
    print(f"{count_sheep} sheep")
else:
    print("None")
