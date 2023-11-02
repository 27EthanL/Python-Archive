# List
pizza_and_prices = [[2, "pepperoni"], [6, "pineapple"], [1, "cheese"], [3, "sausage"], [2, "olives"], [7, "anchovies"], [2, "mushrooms"]]

# Count occurances of 2
num_two_dollar_slices = pizza_and_prices.count(2)

# Length
num_pizzas = len(pizza_and_prices)

# Append
pizza_and_prices.append([2.5, "peppers"])

# Sort
pizza_and_prices.sort()

# Storing
cheapest_pizza = pizza_and_prices[0][1]
priciest_pizza = pizza_and_prices[-1][-1]
three_cheapest = pizza_and_prices[:3]

# Pop
pizza_and_prices.pop()

# Print
print("We sell", num_pizzas, "different kinds of pizza!\n")
print(pizza_and_prices,"\n")
print(three_cheapest)