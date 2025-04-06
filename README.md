# pythonweek3
# Discount Calculator
This Python script calculates the final price of an item after applying a discount.

## Description

The `calculate_discount` function takes the original price and discount percentage as input. If the discount percentage is 20% or higher, the discount is applied, and the final price is returned. Otherwise, the original price is returned.

The script then prompts the user to enter the original price and discount percentage. It calculates the final price using the `calculate_discount` function and prints the result.

## How to Use

1.  **Save the code:** Save the Python code as a `.py` file (e.g., `discount_calculator.py`).
2.  **Run the script:** Open a terminal or command prompt and navigate to the directory where you saved the file. Then, run the script using the following command:
   
    python discount_calculator.py

4.  **Enter input:** The script will prompt you to enter the original price and discount percentage. Enter the values and press Enter.
5.  **View the result:** The script will display the final price after applying the discount (or the original price if no discount was applied).

## Example
Enter the original price: 100
Enter the discount percentage: 25
The final price is: 75.0

Enter the original price: 50
Enter the discount percentage: 10
The final price is: 50.0

## Error Handling

The script includes basic error handling to catch `ValueError` exceptions. If the user enters non-numeric input for the price or discount percentage, an error message will be displayed.

## Function Details

### `calculate_discount(price, discount_percent)`

* **Parameters:**
    * `price`: The original price of the item (float).
    * `discount_percent`: The discount percentage (float).
* **Returns:**
    * The final price after applying the discount (float), or the original price if the discount is less than 20%.

## Requirements

* Python 3.x
