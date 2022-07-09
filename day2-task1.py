 #Book Club Points Serendipity Booksellers
 #prompts the user to input number of books purchased
 #prints points awarded according to number of books purchased
books = int(input("Enter the number of books purchased this month: "))
if (books == 0):
  print("You have been awarded: 0 points\n")
else :
  if (books == 1):
    print("You have been awarded: 6 points\n")
  else :
    if (books == 2):
      print("You have been awarded: 16 points\n")
    else :
      if (books == 3):
        print("You have been awarded: 32 points\n")
      else :
        print("You have been awarded: 60 points")

