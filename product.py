def product_details(product_id, name, quantity, price):
    result = (
        f"Product ID: {product_id}\n"
        f"Product Name: {name}\n"
        f"Quantity: {quantity}\n"
        f"Price: {price}\n"
    )
    return result


if __name__ == "__main__":
    pid = 101
    pname = "laptop"
    quan = 7
    price = 30000
    print(product_details(101, "Laptop", 7, 30000))
