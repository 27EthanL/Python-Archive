# Lovely Loveseat - Furniture
lovely_loveseat_description = ''' 
Lovely Loveseat. Tufted polyester blend on wood. 32 inches high x 40 inches wide x 30 inches deep. Red or white.
'''

# Lovely Loveseat - Price
lovely_loveseat_price = 254.00

# Stylish Settee - Furniture
stylish_settee_description = '''
Stylish Settee. Faux leather on birch. 29.50 inches high x 54.75 inches wide x 28 inches deep. Black.
'''

# Stylish Settee - Price
stylish_settee_price = 180.50

# Luxurious Lamp - Furniture
luxurious_lamp_description = '''
Luxurious Lamp. Glass and iron. 36 inches tall. Brown with cream shade.
'''

# Luxurious Lamp - Price
luxurious_lamp_price = 52.15

# Sales Tax
sales_tax = .088

# Customer One Purchases
customer_one_total = lovely_loveseat_price + luxurious_lamp_price

# Customer One Inventory
customer_one_itemization = lovely_loveseat_description + " " + luxurious_lamp_description

# Sales Tax - Customer One
customer_one_tax = customer_one_total * sales_tax

# Update Cost
customer_one_total += customer_one_tax

# Print Items
print("Customer One Items: ")
print(customer_one_itemization)

# Print Cost
print("Customer One Total: ")
print(customer_one_total)