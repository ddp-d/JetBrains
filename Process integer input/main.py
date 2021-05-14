# put your python code here

while True:
    user_number = int(input())
    if user_number < 10:
        continue
    elif user_number > 100:
        break
    else:
        print(user_number)
