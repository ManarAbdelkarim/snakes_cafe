print("""**************************************
**    Welcome to the Snakes Cafe!   **
**    Please see our menu below.    **
**
** To quit at any time, type "quit" **
**************************************""")

menu = """
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
"""

menu_dic = {
'Wings' :0 ,
'Cookies'  :0,
'Spring Rolls' :0,
'Entrees' :0,
'Salmon' :0,
'Steak':0,
'Meat Tornado' :0,
'A Literal Garden' :0,
'Desserts' :0,
'Ice Cream' :0,
'Cake' :0,
'Pie' :0,
'Drinks' :0,
'Coffee' :0,
'Tea' :0,
'Unicorn Tears' :0
}

def summary():
    print("** Order Summary**")
    for x in menu_dic:
        if menu_dic[x] >0:
            print (f"{menu_dic[x]} order of {x} have been added to your meal")


def take_order():
    x =''
    print(menu)
    while x != 'quit':
        x = input('>')
        if x.capitalize() in menu_dic:
            menu_dic[x.capitalize()]+=1
            print(f"** {menu_dic[x.capitalize()]} order of {x.capitalize()} have been added to your meal **")
        else : 
            print(f"sorry {x} is not in the menu ")
            print("What would you like to order?")
    summary()
    quit()
        
take_order()
