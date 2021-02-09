print("Your Saving Calculator")  # created a string , this the the title
print("                        ")

Per_Hour = input("How much do you earn per hour? £")  #Asks user how much they earn , input always user to enter the amount.
print("                        ")  #Creates a space

Amount_Hour = input("How many hours do you work per day? ")
print("                        ")

Day_input = input("How many days per week? ")  #  input is a function , variables help you save data
print("                        ")

daily_earning = int(Per_Hour) * int(Amount_Hour)  #convert the input into a number using interger
print("How much you earn daily: £", daily_earning)

Weekly_savings = int(daily_earning) * int(Day_input)  #Calculation of daily pay times number of days
print("How much you earn weekly: £", Weekly_savings)  #_ is called snake casing

Monthly_savings = int(Weekly_savings) * 4  #Times 4 for the number weeks in a month
print("How much you earn monthly: £", Monthly_savings)
print("                        ")

Food_perweek = input("How much do you spend on food per week? £")  #Ask user ,what is ther expenses are
print("                        ")

Bills_permonth = input("How much do you spend on bills per month? £")
print("                        ")

Clothes_permonth = input("How much do you spend on clothes per month? £")
print("                        ")

Total_expense = int(Food_perweek) * 4 + int(Bills_permonth) + int(Clothes_permonth)  #Food times the amount of weeks in month , plus bills amount and clothes .To give total expense

print("Your monthly expenses are: £", Total_expense)
print("                        ")

Saving = int(Monthly_savings) - (Total_expense)  #calucates the amount saved/not spent

if Total_expense > Monthly_savings:  # if statement , if Total_expense is greater than Monthly_savings
    print("You need to spend less on expenses!")  # message displayed

elif Total_expense < Monthly_savings:  # if statement , if Total_expense is less than Monthly_savings
    print("Congratulations! Your expenses are less than your earning, Which means you have enough for your saving account. ")
    print("                        ")

    print("You can put £", Saving,"into your saving account")  #The amount saved .
