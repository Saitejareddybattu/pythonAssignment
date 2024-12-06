def calc_bill(*items,**deduction):
  total_bill=0
  for item, price, quantity in Items:
    cost = price * quantity
    total_bill += cost
    print(f"{item}: ${price} x {quantity} = ${cost}")
     
  print(f"Subtotal = {total_bill}")
 
  for key,value in deduction.items():
    if(key=="discount"):
      print(f"You got {value}% Discount!")
      total_bill -= total_bill * (value/100)
 
    if(key=="promo_code"):
      print("Promo Code Applied! $",value)
      total_bill += value
 
    if(key=="delivery_charge"):
      if(total_bill <=500):
        total_bill += value
        print("Bill = ",total_bill)
      else:
        print("You Got Free Delivery!")
        print("Bill = ",total_bill)
   
Items = [("TV", 1000, 2), ("Table", 20, 2), ("Remote", 50, 1)]
 
calc_bill(Items,discount=10,promo_code=-10,delivery_charge=50)