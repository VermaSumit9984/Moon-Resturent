#using dictionary( represented in {}) data type to create menu of restaurant and dictionary is used to store key values 
#defining Menu of restaurant 
Menu={
    'Water':20,
    'Cold drink':20,
    'Maggie':50,
    'Black tea':15,
    'Noraml Tea':20,
    'Passta':60,
    'Veg role':30,
    'Pizza':99,
    'Fried rice':60,
    'Finger':40,
}
#Greet
print("Welcome to restaurant")
print("Water:Rs20\nCold drink:Rs20\nMaggie:50\nBlack tea:15\nNoraml Tea:20\nPassta:60\nVeg role:30\nPizza:99\nFried rice:Rs60\nFinger:Rs40")
 
order_total=0
#using cond statement
item_1=input("enter the name of item you want to order=")
if item_1 in Menu:
    order_total+=Menu[item_1]
    print(f"your item {item_1} has been added to your order")
else:
    print(f"ordered item {item_1} is not available yet!")
    
another_order=input("do you want to add another item?(yes/no)")
if another_order=="yes":
    item_2=input("enter the name of second item=")
    if item_2 in Menu:
        order_total+=Menu[item_2]
        print(f"item {item_2} has been added to order")
    else:
        print(f"ordered item {item_2} is not available!")
        
print(f"The total amount of items to pay is {order_total}")
    
    
    