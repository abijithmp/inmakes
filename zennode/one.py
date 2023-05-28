
#products name and price
products = {'product_A': 20, 'product_B': 40, 'product_C': 50}



#taking inputs of number of quantities
quantity_a = int(input("Enter the quantity of Product A :"))
product_total_a = quantity_a * products['product_A']
# print(product_total_a)

quantity_b = int(input("Enter the quantity of Product B :"))
product_total_b = quantity_b * products['product_B']
# print(product_total_b)

quantity_c = int(input("Enter the quantity of Product C :"))
product_total_c = quantity_c * products['product_C']
# print(product_total_c)


#details include total product amount,price,name
thisdict = {
    "product_A": [product_total_a, quantity_a, products['product_A']],
    "product_B": [product_total_b, quantity_b, products['product_B']],
    "product_C": [product_total_c, quantity_c, products['product_C']]
}
cart_total = product_total_c + product_total_b + product_total_a

# print("cart total", cart_total)
total_quantity = quantity_a + quantity_b + quantity_c

#taking input to gift wrap
gift = int(input("How many units to  gift wrap in {a} units : ".format(a=total_quantity)))

#empty list to collect cart totals based on discounts
lst_1 = []
cart_total_1 = 0
cart_total_3 = 0
cart_total_4 = 0
cart_total_2 = 0

#function to calculate discounts
def disocunt(cart_total, thisdict):
    cart_total_1 = 0
    cart_total_3 = 0
    cart_total_4 = 0
    cart_total_2 = 0

    if cart_total > 200:
        cart_total_1 = cart_total - 10
        # print("total amount after dis_1 :", cart_total_1)
        lst_1.append(cart_total_1)
    s=0
    for i in thisdict:


        if thisdict[i][1] > 10:
            # print("quantity", thisdict[i][1])
            dis = thisdict[i][0] * 0.05
            s = s + dis
            # print("5% dis", dis,s)
            cart_total_2 = cart_total - s

    if cart_total_2 > 0:
        # print("cart total after dis_2:", cart_total_2)
        lst_1.append(cart_total_2)

    if total_quantity > 20:
        d2 = cart_total * .1
        # print("10% dis :", d2)
        cart_total_3 = cart_total - d2
        # print("cart total after dis_3:", cart_total_3)
        lst_1.append(cart_total_3)
    d = 0
    for i in thisdict:

        if total_quantity > 30 and thisdict[i][1] > 15:
            extra = thisdict[i][1] - 15
            # print("extra quantity :", extra)
            # print("extra quantity amount :", extra * thisdict[i][2])
            dis = extra * thisdict[i][2]*.5
            d = d + dis
            # print("fict", dis)
            cart_total_4 = cart_total - d
    if cart_total_4 > 0:
        # print("cart total after dis_4:", cart_total_4)
        lst_1.append(cart_total_4)
    # print(lst_1)
    # print(min(lst_1))
    if cart_total_1 == min(lst_1):
        print("Discount Name : flat_10_discount *** Discount Amount : {a} {b}".format(a=cart_total - cart_total_1,b="$"))
    elif cart_total_2 == min(lst_1):
        print("Discount Name : bulk_5_discount *** Discount Amount : {a} {b}".format(a=cart_total - cart_total_2,b="$"))
    elif cart_total_3 == min(lst_1):
        print("Discount Name : bulk_10_discount *** Discount Amount : {a} {b}".format(a=cart_total - cart_total_3,b="$"))
    else:
        print("Discount Name : tiered_50_discount *** Discount Amount : {a} {b}".format(a=cart_total - cart_total_4,b="$"))


ship = 0

#function to calculate ship fee
def ship_1(total_quantity):
    ship = (total_quantity // 10) * 5
    oddone = total_quantity % 10
    # print(oddone)
    if oddone != 0:
        return ship + 5
    else:
        return ship


# disocunt(cart_total, thisdict)

# print("shipcharge :", ship_1(total_quantity))


#printing the output
print("*******")
print("Out Put")
print("*******")
for x, y in thisdict.items():
    print("Product name : {a} *** Quantity: {b}  *** Total Amount of that Product: {c} {d}".format(a=x
                                                                                               , b=y[1],
                                                                                               c=y[0],d="$"))

print("*******")
print("SubTotal : {a} {b} ".format(a=cart_total, b="$"))
print("*******")
disocunt(cart_total, thisdict)
print("*******")
print("shipcharge : {a} {b}".format(a=ship_1(total_quantity),b="$") )
print("*******")
if gift != 0:
    cart_total_5 = min(lst_1) + gift + ship_1(total_quantity)
    print("gift wrap fee  : {a} {b}".format(a=gift,b="$") )
    print("*******")
    print("Total Fee : {a} {b}".format(a=gift + ship_1(total_quantity),b="$") )
    print("*******")
    print("Total Amount: {a} {b}".format(a=cart_total_5,b="$"))

else:
    cart_total_5 = min(lst_1) + gift + ship_1(total_quantity)
    print("gift wrap fee  : {a} {b}".format(a=gift, b="$"))
    print("*******")
    print("Total Fee : {a} {b}".format(a=gift + ship_1(total_quantity), b="$"))
    print("*******")
    print("Total Amount: {a} {b}".format(a=cart_total_5, b="$"))
