print ("""
Hi this is shopping basket
You can purcahse anything
""")
shopping_basket={}
option = int(input("Enter an option:"))

while option!= exit:
    if option ==1:
        item = input("Enter the item:")
        if item in shopping_basket:
            print("Item already exists in te basket")
            qnty = input("Enter the quantity:")
            shopping_basket[item] = shopping_basket[item]+qnty
        qnty = input("Enter the quantity:")
        shopping_basket[item] = qnty
    elif option==2:
        item = input("Enter an item")
        del(shopping_basket[item])
    elif option==3:
        for item in shopping_basket:
            print(item,":",shopping_basket[item])
    elif option!=exit:
        print("You emtered wrong number..")
    option = int(input("\n\n Enter an option")) 

else:
    print("Shopping closed")


            