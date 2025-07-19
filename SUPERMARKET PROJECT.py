from datetime import datetime
name = input("Enter your name: ")
LISTS = '''
RICE    RS 20/KG
SUGAR   RS 30/KG
SALT    RS 20/KG
OIL     RS 80/LITER
PANEER  RS 110/KG
MAGGIE  RS 50/KG
BOOST   RS 90/EACH
COLGATE RS 45/EACH  '''
#declaration
price = 0
listprice =[]
totalprice = 0
finalprice = 0
itemlist =[]
quantitylist =[]
pricelist = []
#rates of items
items ={"rice":20,"sugar":30,"salt":20,"oil":80,"panneer":110,"maggie":50,"boost":90,"colgate":45}
option =int(input("Click the number 1 : "))
if option == 1:
    print(LISTS)
for i in range(len(items)):
    a =int(input("If you want to buy product press 1 and exit for 2: "))
    if a == 1:
        item = input("Enter your item :")
        quantity = int(input("enter your quantity:" ))
        if item in items:
            price = quantity*(items[item])
            listprice.append((item,quantity,items,price))
            totalprice+=price
            itemlist.append(item)
            quantitylist.append(quantity)
            pricelist.append(price)
            gst = (totalprice*5)/100
            finalprice = gst*totalprice
        else:
            print("Your item not avaliable")
    else:
        print("you enter incorrect pin")
    a =input("If you want bill press yes otherwise no: ")
    if a != "yes":
        break
    if a == "yes":
        if finalprice!=0:
            print(25*"=","SUPER MARKET",25*"=")
            print(28*" ","praveen",28*" ")
            print("NAME:",name,30*" ","date:",datetime.now())
            print(50*"-")
            print("s:no",8*" ","items:",item,8*" ","Quantity",quantity,3*" ","price:",totalprice)
            print(50*" ")
            print(50*" ","GST:",gst)
            
                
          
 

   
