#Find the amount after discount

"""Suppose you are a university student, and you need to pay 4535 dollars tuition fee for the next semester. 
The college is giving you a discount of 10% on the early payment of your tuition fee. 
Since it's a good offer, you decided to make an early payment. 
Can you find out how much money you have to pay?"""

fee = 4535
discount = 10/100
early_payment= (fee - ((fee*discount)))
print("You will be charged $", early_payment)
