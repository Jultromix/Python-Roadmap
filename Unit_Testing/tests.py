def calculate_total(products):
    total = 0
    for product in products:
        total += product["price"]
    return total


def test_calculate_total_with_empty_list():
    assert calculate_total([]) == 0


def test_calculate_total_with_single_product():
    products = [{"name": "Product A", "price": 10}]

    assert calculate_total(products) == 10


def test_calculate_total_with_multiple_product():
    products = [
        {"name": "Product A", "price": 10},
        {"name": "Product B", "price": 20},
        {"name": "Product C", "price": 30},
    ]

    assert calculate_total(products) == 60


if __name__ == "__main__":
    test_calculate_total_with_empty_list()
    test_calculate_total_with_single_product()
    test_calculate_total_with_multiple_product()
    print("All tests passed!")
