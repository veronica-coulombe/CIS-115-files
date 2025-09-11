print("Hello!")

startingAmount = float(input("What is the starting gift card amount?\n "))

print("Your gift card amount is ", startingAmount)

purchaseAmount = float(input("What is the purchase amount?\n "))

tax = .06 * purchaseAmount

total = purchaseAmount + tax

print(f'Your total is {total:.2f}')

giftCard = startingAmount - total

print(f'You have {giftCard:.2f} left in you gift card.')

purchaseAmount2 = float(input("What is the second purchase amount?\n "))

tax2 = .06 * purchaseAmount2

total2 = purchaseAmount2 + tax2

print(f'Your total is {total2:.2f}')

giftCard2 = giftCard - total2

print(f'You have {giftCard2:.2f} left in you gift card.')

print("Thank you!")