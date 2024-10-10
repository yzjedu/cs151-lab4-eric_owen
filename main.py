def calculate_mobile_bill():
    # Ask the user for their package choice
    package = input("Enter your package (Green, Blue, or Purple): ").lower()

    # Validate package input
    while package not in ['green', 'blue', 'purple']:
        print("Invalid input. Please choose Green, Blue, or Purple.")
        package = input("Enter your package (Green, Blue, or Purple): ").lower()

    # If package is green
    if package == 'green':
        # Constants for Green package
        base_price = 49.99
        data_included = 2
        additional_gb_rate = 15

        # Ask user for additional GBs used
        additional_gb = int(input("Enter the additional GB you used: "))
        total_gb = data_included + additional_gb
        gb_cost = additional_gb * additional_gb_rate
        price = base_price + gb_cost

        # Ask if user has a coupon
        coupon = input("Do you have a coupon? (yes or no): ").lower()
        if coupon == 'yes' and price > 75:
            price -= 20

        print(f"Total GB used: {total_gb}GB, Total price: ${price:.2f}")

    # If package is blue
    elif package == 'blue':
        # Constants for Blue package
        base_price = 70
        data_included = 4
        additional_gb_rate = 10

        # Ask user for additional GBs used
        additional_gb = int(input("Enter the additional GB you used: "))
        total_gb = data_included + additional_gb
        gb_cost = additional_gb * additional_gb_rate
        price = base_price + gb_cost

        print(f"Total GB used: {total_gb}GB, Total price: ${price:.2f}")

    # If package is purple
    elif package == 'purple':
        # Constants for Purple package
        price = 99.95
        print(f"Unlimited data, Total price: ${price:.2f}")


# Run the function
calculate_mobile_bill()
# Read the README.md
# Read it again
# Your code here
# Delete these 4 lines of comments
