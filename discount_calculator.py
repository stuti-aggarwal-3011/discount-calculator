def apply_discount(price, discount):
    # Check if price is a valid number
    if type(price) is not int and type(price) is not float:
        return "The price should be a number"
        
    # Check if discount is a valid number
    if type(discount) is not int and type(discount) is not float:
        return "The discount should be a number"
        
    # Ensure price is greater than zero
    if price <= 0:
        return "The price should be greater than 0"

    # Ensure discount is within valid percentage range
    if discount < 0 or discount > 100:
        return "The discount should be between 0 and 100"
    
    # Calculate and return the discounted price
    return price - discount*price/100

# Test cases
apply_discount(100,20)
apply_discount(200,50)
apply_discount(500,100)
