weight = 41.5
gsfc = 20
gspfc = 125.0

# Ground Shipping
if weight <= 2:
  print("Ground Shipping:", "$" + str((weight * 1.50) + gsfc))
  print("Ground Shipping Premium:", "$" + str(gspfc))
elif weight > 2 and weight <= 6:
  print("Ground Shipping:", "$" + str((weight * 3.00) + gsfc))
  print("Ground Shipping Premium:", "$" + str(gspfc))
elif weight > 6 and weight <= 10:
  print("Ground Shipping:", "$" + str((weight * 4.00) + gsfc))
  print("Ground Shipping Premium:", "$" + str(gspfc))
elif weight > 10:
  print("Ground Shipping:", "$" + str((weight * 4.75) + gsfc))
  print("Ground Shipping Premium:", "$" + str(gspfc))

# Drone Shipping
if weight <= 2:
  print("Drone Shipping:", "$" + str(weight * 4.50))
elif weight > 2 and weight <= 6:
  print("Drone Shipping:", "$" + str(weight * 9.00))
elif weight > 6 and weight <= 10:
  print("Drone Shipping:", "$" + str(weight * 12.00))
elif weight > 10:
  print("Drone Shipping:", "$" + str(weight * 14.25))