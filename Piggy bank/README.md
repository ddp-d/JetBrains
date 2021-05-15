Piggy bank

You are given a class PiggyBankthat represents an old-school moneybox in the shape of a pig. It has two attributes, dollars and cents, and their initial values are passed to the constructor.

Create a method add_money with two parameters, deposit_dollars and deposit_cents, that increases the sum of money in the piggy bank. To put it another way, in the method, you are supposed to increase the values of dollars and cents by deposit_dollars and deposit_cents respectively.

Parameters deposit_dollars and deposit_cents of the add_money method can have any value, but the value of the attribute cents cannot be higher than 99!

For example, we start with PiggyBank(0, 50): 0 dollars and 50 cents. If we try to add another 50 cents, we will have to update the values of both dollars and cents, because the attribute cents cannot equal 100. So, the resulting values are 1 dollar and 0 cents.

NOTE: you do NOT need to process input. The examples below are for you to test your program. The input shows how many dollars and cents we add to the piggy bank with 1 dollar and 1 cent. The output is the resulting amount of money.


Sample Input:
0 99

Sample Output:
2 0


Sample Input:
0 88

Sample Output:
1 89


Sample Input:
500 500

Sample Output:
506 1
