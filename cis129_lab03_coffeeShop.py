#Hector Silva
# this script is for the module 3 lab and it creates an interactive text based Coffee Shop simulator that calculates a receipt based on how many items the user wants to order.

print('welcome to the module 3 cafe!)

#numC stands for the number of coffees bought
numC= input('How many coffees would you like to buy?)

#numM stands for the number of muffins bought
numM= input('and how many muffins would you like to buy?')

#the next steps create variables for the price of one coffee and one muffin then calculate the total cost of the users order without tax.

pcoffee=5
pmuffin=8
taxless_total=pcoffee*numC+pmuffin*numM

#the next step creates the variable Total and the sales tax variable sales_tax then adds tax to the taxless_total
sales_tax=0.06
Total=(sales_tax+1)*taxless_total

print('Thank you for your order. your total is $', Total, 'your order will be ready soon.'/n 'Thank you for visiting the module 3 lab cafe!')
print('We hope you come again soon!.')
