# Lists
hairstyles = ["bouffant", "pixie", "dreadlocks", "crew", "bowl", "bob", "mohawk", "flattop"]
prices = [30, 25, 40, 20, 20, 35, 50, 35]
last_week = [2, 3, 5, 8, 4, 4, 6, 2]
new_prices = [price - 5 for price in prices]
cuts_under_30 = [hairstyles[i] for i in range(0, len(new_prices) - 1) if new_prices[i] < 30]

# Variables
total_price = 0
total_revenue = 0

# Functions
for price in prices:
  total_price += price
for i in range(0, len(hairstyles)):
  total_revenue += prices[i] * last_week[i]

# Math
average_price = round(total_price / len(prices), 2)
average_daily_revenue = total_revenue / 7

# Prints
print(new_prices)
print(cuts_under_30)
print("Average Haircut Price:", average_price)
print("Total Revenue:", total_revenue)
print("Average Daily Revenue:", average_daily_revenue)