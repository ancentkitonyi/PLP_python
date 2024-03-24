# Create a function named calculate_discount(price, discount_percent) that calculates the final price after applying a discount.
# The function should take the original price (price) and the discount percentage (discount_percent) as parameters. 
# If the discount is 20% or higher, apply the discount; otherwise, return the original price.
# Using the calculate_discount function, prompt the user to enter the original price of an item and the discount percentage. 
# Print the final price after applying the discount, or if no discount was applied, print the original price.

def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        new_price = price - (0.2*price)
        print("Discount Applied! Final price is: {}".format(new_price))
    else:
        print("No discount applied! Final price: {}".format(price))
        
price = float(input("Enter the original price: "))
discount_percent = float(input("Enter the discount percentage: "))

calculate_discount(price, discount_percent)