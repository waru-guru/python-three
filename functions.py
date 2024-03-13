
def calculate_dicount(price,discount_percent): 
    

    if discount_percent > 20:
        discount_amount = price * (discount_percent / 100)
        new_price = price - discount_amount
        return new_price
    else:
        return price
    
price = float(input("Enter price: "))
discount_percent = float(input("Enter percentage of discount : "))

updated_price = calculate_dicount(price,discount_percent)

if updated_price == price:
    print("Discount not applied, discount percentage lower than 20. Price is: ", updated_price)
else:
    print("Price after discount: ", updated_price)

        
