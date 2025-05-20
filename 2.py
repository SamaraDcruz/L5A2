# Step 1: Ask the user for buying and selling prices
cost_price = int(input("Enter the cost price: "))
selling_price = int(input("Enter the selling price: "))

# Step 2: Check for profit or loss
if selling_price > cost_price:
    profit = selling_price - cost_price
    print("You made a profit of", profit, "rupees! 🎉")

elif selling_price < cost_price:
    loss = cost_price - selling_price
    print("Oops! You had a loss of", loss, "rupees. 😞")
else:
    print("No profit, no loss. You broke even! 🙂")