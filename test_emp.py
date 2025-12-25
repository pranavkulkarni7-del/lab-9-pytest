from product import product_details

def test_product_details():
    output = product_details(101, "Laptop", 5, 55000)

    expected = (
        "Product ID: 101\n"
        "Product Name: Laptop\n"
        "Quantity: 5\n"
        "Price: 55000\n"
    )

    assert output == expected
