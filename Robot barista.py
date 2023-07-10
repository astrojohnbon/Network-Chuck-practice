#Lets start a coffee shop together!

#Lets build a robot barista

print("Hello, welcome to networkchuck coffee!!")

name = input("What is your name? \n")

if name == "Ben":
    evil_status = input("Are you evil?")
    if evil_status == "yes":
        print("You're not welcome here EVIL BEN! Get out!")
        exit()
else: 
    print("Hello " + name + ", thank you so much for coming in today")
    
menu = "black coffee, flat white, espresso, latte"

print( "Ok " + name + " What can I get started for you? Today we are serving: \n" + menu)

order = input()

if order == "black coffee":
    price = 3
elif order == "flat white":
    price = 5
elif order == "latte":
    price = 6 
elif order == "espresso":
    price = 4
else:
    print("Sorry, we don't have that here.")

quantity = input("How many coffees would you like? \n")

total = price * int(quantity)
print("Thank you. " + name + " Your total is: $" +  str(total) + " I'll get your " + quantity + " " + order +  
      " started right away!")



      
