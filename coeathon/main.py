day = 0
order = input()
orders = int(order)
while orders > 0:


    if orders % 2 == 0:

        if (orders / 2) % 2 !=0 and (orders / 2) % 3 !=0:
            orders -= 1
            day += 1
        else :
            orders = orders - (orders / 2)
            day += 1
    elif orders % 3 ==0:
        orders = orders - (2*(orders/3))
        day += 1
    else:
        orders = orders - 1
        day += 1

print(day)



