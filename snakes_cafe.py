Appetizers = ["Wings","Cookies","Spring Rolls"]



def intro():
    print('''
**************************************
**    Welcome to the Snakes Cafe!   **
**    Please see our menu below.    **
**
** To quit at any time, type "quit" **
**************************************

Appetizers
----------
Wings
Cookies
Spring Rolls

Entrees
-------
Salmon
Steak
Meat Tornado
A Literal Garden

Desserts
--------
Ice Cream
Cake
Pie

Drinks
------
Coffee
Tea
Unicorn Tears

***********************************
** What would you like to order? **
***********************************
''')
          
def user_insertion():
    user_input=input(">")
    return user_input

def end_app():
    print("thanks")

def main():
    user_input = user_insertion()
    while(user_input.lower() !="quit"):
        if user_input in Appetizers:
          print("you have added")
          print(Appetizers.count(user_input))
          print(user_input)
          #TODO: handle the order number
        else:
          print("sorry we didint have this item")
        user_input = user_insertion()
    end_app()   


intro()
main()







   
