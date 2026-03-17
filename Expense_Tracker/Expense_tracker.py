from expense import expense
from typing import List
import calendar
import datetime


def main():
    print(f"Running Expense Tracker")
    expense_file_path="expense.csv"
    budget= int(input("enter your budget"))
    
    # get user to input there expense
    expense =  get_user_expense()
  
     #write expense to the file
    save_expense_to_file(expense, expense_file_path)


     #read the file and summerise  the expence.
    summerise_expense( expense_file_path,budget)


def get_user_expense(): 
    print(f"getting user Expense")
    expense_name=input("enter the expense name :")
    expense_amount= float (input("enter the expense amount :"))
    expense_categories=[
        "🍎food",
        "🏚️home",
        "👩‍⚕️work",
        "🎉fun",
        "🥹misc"
        ]

    while True: 
        print("select a category:")
        for i,category_name in enumerate(expense_categories):
            print(f"  {i+1}.{category_name}")

        value_range = f"[1-{len(expense_categories)}]"
        
        selected_index= int(input(f"Enter a category number{value_range}:"))-1

        if selected_index in range(len(expense_categories)):
            selected_category = expense_categories[selected_index]
            new_expense = Expense(name=expense_name , category=selected_category,amount=expense_amount)
            return new_expense
        else:
            print("invalid category .Please try again")







        
def save_expense_to_file(expense:Expense,expense_file_path):
    print(f"saving user Expense :{expense} to {expense_file_path}")
    with open (expense_file_path,"a",encoding="utf-8")as f:
        f.write(f"{expense.name},{expense.amount},{expense.category}\n")
   

def summerise_expense(expense_file_path ,budget): 
    print(f"summerise user expense")
    expenses:List[Expense] = []
    with open(expense_file_path,"r",encoding="utf-8") as f:
        lines=f.readlines()
        for line in lines:      
            
         

            expense_name,expense_amount,expense_category = line.strip().split(",")
            print( expense_name,expense_amount,expense_category)
            line_expense = Expense(name=expense_name,
                                amount=float(expense_amount),
                                category=expense_category
                                )
       
            expenses.append(line_expense)
            amount_by_category = {}
        for expense in expenses:
           key=expense.category
           if key in amount_by_category:
               amount_by_category[key] += expense.amount 
           else:
               amount_by_category[key]= expense.amount 

        print("Expense by category📈")
        for key, amount in amount_by_category.items():
          print(f"  {key}: {amount:.2f}")


        total_spent = sum([x.amount for  x in expenses])   
        print(f"Total spent🛒: {total_spent:.2f}this month!")


     
    
        remaining_budget = budget - total_spent
        print(f"buget remaining💶:{remaining_budget:.2f}")


        #get the current date
        now =datetime.datetime.now()

        #get the no. of days in the current months
        days_in_months =calendar.monthrange(now.year,now.month)[1]
    
        # calculating the remaining number of days in the current month
        remaining_days =days_in_months - now.day

        daily_budget = remaining_budget/remaining_days
        print(green(f"👉budget per days:{daily_budget:.2f}"))

def green(text):
    return f"\033[92m]{text}\033[0m"



if __name__== "__main__":
    main()