# calculate_discount.py

def calculate_discount(price, discount_percent):
    """
    Calculate the final price after applying a discount if the discount is 20% or higher.

    Parameters:
        price (float): Original price of the item.
        discount_percent (float): Discount percentage to be applied.

    Returns:
        float: Final price after discount or the original price if the discount is less than 20%.
    """
    if discount_percent >= 20:
        discount_amount = (discount_percent / 100) * price
        return price - discount_amount
    return price


if __name__ == "__main__":
    try:
        # Prompt user for input
        price = float(input("Enter the original price of the item: "))
        discount_percent = float(input("Enter the discount percentage: "))

        # Calculate the final price
        final_price = calculate_discount(price, discount_percent)

        # Print the result
        if discount_percent >= 20:
            print(f"The final price after applying the discount is: ${final_price:.2f}")
        else:
            print(f"No discount applied. The original price is: ${price:.2f}")
    except ValueError:
        print("Invalid input. Please enter numeric values for price and discount percentage.")
