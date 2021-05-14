user_input = int(input())

if user_input == 1:
    print("This number is not prime")
elif user_input > 1:
    for i in range(2, user_input):
        if (user_input % i) == 0:
            print("This number is not prime")
            break
    else:
        print("This number is prime")
