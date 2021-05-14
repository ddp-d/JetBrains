income = int(input())

percent = 0
calculated_tax = 0

if 0 <= income <= 15527:
    percent = 0
    calculated_tax = income * percent / 100
elif 15527 < income <= 42707:
    percent = 15
    calculated_tax = income * percent / 100
elif 42707 < income <= 132406:
    percent = 25
    calculated_tax = income * percent / 100
else:
    percent = 28
    calculated_tax = income * percent / 100

print(f"The tax for {income} is {percent}%. That is {calculated_tax:.0f} dollars!")
