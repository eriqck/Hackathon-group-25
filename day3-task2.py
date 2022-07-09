#function to calculate fat calories

def fat_calories():
  fat_grams = int(input("Enter number of fat grams  consumed in a day\n"))
  fat_carl = (fat_grams * 9)
  print("The patient has", fat_carl, "fat calories")

#function to calculate carbohhdrates calories

def carb_calories():
  carb_grams = int(input("Enter number of carbohydrates grams consumed in a day\n"))
  carb_carl = (carb_grams * 4)
  print("The patient has", carb_carl, "carbohydrates calories")

# calls the functions fat_calories() and carb_calories()

fat_calories()
carb_calories()
