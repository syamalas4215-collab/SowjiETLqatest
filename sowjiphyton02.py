#numbers = [13,16,23,15,4,66]
#for number in numbers:
#    print(number)
#    if  number % 2 == 0:
#        print(number,"is even")
#    else:
#        print(number,"is odd")

dict_items_number = {
    "pasta":{"price":6,"quantity":3},
    "rice": {"price":25,"quantity":5},
    "potatos": {"price":7,"quantity":10},
    "chips":  {"price": 5,"quantity":4}
}
total = sum(items["price"]  *  items["quantity"] for items in dict_items_number.values())
print(total)
dict_items_number["apples"] = {"price": 5,"quantity": 4}
dict_items_number["bananas"] = {"price": 2,"quantity": 3}
print(dict_items_number)




