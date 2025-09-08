print("Hello, welcome to Whole Foods!")

baconPrice = float(input("What is the price of bacon?\n "))
cakePrice = float(input("What is the price of cake?\n "))
saladPrice = float(input("What is the price of salad?\n "))
chipsPrice = float(input("What is the price of chips?\n "))

subtotal = baconPrice + cakePrice + saladPrice + chipsPrice

tax = .06 * subtotal

total = subtotal + tax

print("Your subtotal is going to be ", subtotal)

print("Your tax for today is going to be ", tax)

print("That brings your total to ", total)

print("Thank you for shopping!")