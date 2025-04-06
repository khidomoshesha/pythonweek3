def calculate_discount(price, discount_percent):
    """
    Calculates the price after a discount.

    If the discount is 20% or more, it applies the discount.
    Otherwise, it returns the original price.
    """

    if discount_percent >= 20:
        # Calculate the discount amount
        discount_amount = (discount_percent / 100) * price

        # Subtract the discount from the original price
        final_price = price - discount_amount

        # Return the final price
        return final_price
    else:
        # If the discount is less than 20%, return the original price
        return price

# Ask the user for the original price
price_input = input("Enter the original price: ")

# Try to convert the input to a number
try:
    price = float(price_input)

    # Ask the user for the discount percentage
    discount_input = input("Enter the discount percentage: ")

    # Try to convert the input to a number
    try:
        discount_percent = float(discount_input)

        # Calculate the final price using the function
        final_price = calculate_discount(price, discount_percent)

        # Print the final price
        print("The final price is:", final_price)

    except ValueError:
        print("Invalid discount percentage. Please enter a number.")
except ValueError:
    print("Invalid price. Please enter a number.")