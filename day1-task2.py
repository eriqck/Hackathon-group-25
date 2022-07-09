#prompts user to input square feet to be painted
sq_ft = float(input("Enter the square feet of wall space to be painted\n"))
price = float(input("Enter the price of paint per gallon\n"))

#function to calculate gallons of paint required
def gallons_required():
  gallons = sq_ft/115
  print("The number of gallons of paint required\n", gallons)

#function to calculate hours required to paint
def hours_required():
  hrs = (sq_ft*8)/115
  print("The hours of labour required\n", hrs)

#function to determine cost of paint
def paint_cost():
  paint_cost = price * (sq_ft/115)
  print("The cost of the paint\n", paint_cost)

#function to determine labor charges
def labor_charges():
  labor = ((sq_ft*8)/115) * 20
  print("The labor charges\n", labor)

#function to determine total cost
def total_cost():
 t_cost =  (((sq_ft*8)/115)*20) + (price*(sq_ft/115))
 print("The total cost of the paint job\n", t_cost)

#calling the functions
gallons_required()
hours_required()
paint_cost()
labor_charges()
total_cost()
