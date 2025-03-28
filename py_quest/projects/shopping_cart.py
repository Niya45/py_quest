cart = []
prices = []
price = 0.0

while True:
    food = input("What food would you like to buy (q to quit): ")
    if food.lower() == "q":
        break
    else:
        cost = float(input("What is the price of the food : $"))
        cart.append(food)
        prices.append(cost)

print("____YOUR CART______")

if cart:
    for i in range(len(cart)):
        print(cart[i], end=" ")
        price += prices[i]
print()
print(f"- Total cost: {price}")
    