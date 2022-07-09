#function menu prompts the user to choose for career advice or to ask a question
def menu():
  print ("************************************\n")
  print ("1. Career advices\n")
  print ("2. Career questions\n")
  print ("**************************************")

#function c_a() which means career advice contains a list advice with career advices. user is prompted to enter career to persue and a corresponding advice is printed
def c_a():
  c = str(input("Available career choices: Web Development, Data Scientist, UI/UX Designer. Type your choice \n"))
  advice = ["To be venture in web development career, you need HTML, JAVASCRIPT and CSS skills. This can be achieved through free online resources, colleges or bootcamps", "To venture a career as a data scientist, you need to have powerful skills in python programming. This will enable you to learn machine learning and data analytics which are the core skills of a data scientist", "To be an UI/UX designer, you dont need to have programming skills though having them is an added advantage. UI/UX designers are one of the highest paid developers today. You can become one within four months through free online resources and websites"]

  if (c == "Web Development"):
    print(advice[0])
  else :
    if (c == "Data Scientist"):
      print(advice[1])
    else :
      if(c == "UI/UX Designer"):
        print(advice[2])
      else :
        print("Invalid input")

#function career question enables user to ask a question
def c_q():
  questions = int(input("FAQs: 1. Front-end or back-end, 2. Most paid"))
  advices = ["Learn both front-end and back-end", "Back-end is most paid "]
  if questions == 1:
    print(advices[0])
    print("I would advice you persue a career as a back end engineer")
  if questions == 2:
    print(advices[1])
    print("I would advice you persue a career as a front-end engineer")


#calls the menu function
menu()

#prompts user for a menu option
option = input("choose an option from the above menu: \n")

if option == "1":
    c_a()
if option == "2":
    c_q()
if option == "3":
  print("ivalid option")
