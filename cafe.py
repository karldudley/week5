# list of cafe items
menu = ["Bacon Bap", "Doughnut", "Oatcake", "Smoothie", "Hot Choc"]

# dictionary of stock
stock = {"Bacon Bap": 10,
         "Doughnut": 12,
         "Oatcake": 6,
         "Smoothie": 15,
         "Hot Choc": 20
        }

# dictionary of prices
price = {"Bacon Bap": 3.99,
         "Doughnut": 2.50,
         "Oatcake": 1.99,
         "Smoothie": 0.99,
         "Hot Choc": 1.20
        }

# print stock on hand
print(f"ITEM\t\tQUANTITY\tPRICE(£)\tTOTAL STOCK WORTH(£)")
for x in menu:
    print(x,"\t",stock[x],"\t\t",price[x],"\t\t",round(stock[x]*price[x],2))
