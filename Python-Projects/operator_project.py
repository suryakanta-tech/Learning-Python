# project

customer_name = "Suryakanta Pradhan"
print("Customer Name: ",customer_name) # name of the customer

item_list = ['laptop','mobile','mouse','keyboard','camera'] # items list
item_price = [50000,35000,5000,1500,20000] # items price
length = len(item_price) # length of items price

# total_bill = (item_price[0]+item_price[1]+item_price[2]+item_price[3]+item_price[4])

total_bill = sum(item_price) # sum of items price
average = total_bill / length
print("Total Bill: ",total_bill) # print the total items bill
print("Average Price: ",average) # print the total items average price

if total_bill <= 10000:
  delivery_charge = 0
elif total_bill <=50000:
  delivery_charge = 50
elif total_bill <=100000:
  delivery_charge = 100
elif total_bill <=200000:
  delivery_charge = 200
else: 
  delivery_charge = 300 
final_bill = total_bill + delivery_charge # add the delivery charge with total items price
print("Final Bill: ",final_bill) # final bill : total items price + delivery charge

print("Total >= 50000: ",total_bill >= 50000)
print("Average: ",average >= 5000)

# check category of the customer 
if total_bill >= 100000:
  print('Category: Most Premium Customer')
elif total_bill >= 50000:
  print('Category: Premium Customer')
else:
  print('Category: Normal Customer')

x = ('mobile' in item_list) # check this perticular item is present in the list
y = ('speaker' not in item_list) # check this perticular item is not present in this list
print("Mobile in item list: ",x)
print("Speaker not in item list: ",y)



