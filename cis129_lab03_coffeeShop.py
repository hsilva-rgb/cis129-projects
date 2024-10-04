#Hector Silva
#contact info
#10/03/2024

#this script is for the module 3 lab and it creates an interactive/
#text based Coffee Shop simulator that calculates a receipt based on /
#how many items the user wants to order.

#10/03/2024 some typos removed and 2 items added to the menu

print('welcome to the module 3 cafe!')

#numC stands for the number of coffees ordered by the user
numC = int(input('How many coffees would you like to buy?'))
#numM stands for the number of muffins ordered by the user
numM = int(input('How many muffins would you like to buy?'))
#numB stands for the number of brownies ordered by the user
numB = int(input('How many brownies would you like to buy?'))
#numF stands for the number of fruit cups ordered by the user
numF = int(input('and how many fruit cups would you like to buy?'))

#the next steps create variables for the price of one coffee, /
#one muffin, one brownie, and one fruit cup then calculate the total cost /
#of the users order without tax
pcoffee = int(5)
pmuffin = int(4)
pbrownie = float(3.5)
pfruitcup = float(3)
taxless_total = int((pcoffee * numC) + (pmuffin * numM) + (pbrownie * numB)/
                    (pfruitcup *numF))

#the next step creates the variable Total and the sales tax variable sales_tax/
#then adds tax to the taxless_total
sales_tax = float(0.06*taxless_total)
Total = float((sales_tax + taxless_total))
round(Total, 2)
round(sales_tax, 2)
print('Module 3 cafe reciept')
print(numC, ' cups of coffee')
print(numM, ' muffin(s)')
print(numB, 'brownie(s)')
print(numF, 'fruit cup(s)')
print('sales tax at 6%', sales_tax)
print('Your total is $',Total)
print('Thank you for your order.')
print('We hope you come again soon!')
