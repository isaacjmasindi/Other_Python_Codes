#
#shop_list is valued to the items in the cafe
#stock list is a list of the stock value of the items 
#price_list is a list of the price of the items
shop_list= ["Muffins","Bread","Coffe","Orange juice"]

stock_list= [200.00,335.00,150.00,234.00]

price_list= [35.00,45.00,30.00,35.00]

#a dictionary is created using the shop_list and stock_list
#a dictionary is created using the shop_list and price_list
stock_dictionary= dict(zip(shop_list,stock_list))


price_dictionary= dict(zip(shop_list,price_list))


#the for loop is used to minus the stock value and the price to get the total stock worth for each stock
#total_for_all is vauled to zero and keeps being added to the total stock for each item in the cafe as long as the loop runs
total_for_all=0
for (key,value),(key2,value2) in zip(stock_dictionary.items(),price_dictionary.items()):
    print(f" the total stock worth for {key} is R{value*value2}")
    total_for_all+=value*value2

print(f"the total stock for all the stock is R{total_for_all}")
        
