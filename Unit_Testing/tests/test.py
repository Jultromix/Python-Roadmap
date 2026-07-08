def calculate_total(products, discount=0):
    total = 0
    for product in products:
        total += product["price"] - (product["price"] * discount)
    return total


def test_calculate_total_with_empty_list():
    assert calculate_total([]) == 0
    assert calculate_total([], discount=0.5) == 0


def test_calculate_total_with_single_product():
    products = [{"name": "Product A", "price": 10}]

    assert calculate_total(products) == 10
    assert calculate_total(products, discount=0.5) == 5


def test_calculate_total_with_multiple_product():
    products = [
        {"name": "Product A", "price": 10},
        {"name": "Product B", "price": 20},
        {"name": "Product C", "price": 30},
    ]

    assert calculate_total(products) == 60
    assert calculate_total(products, discount=0.5) == 30


if __name__ == "__main__":
    test_calculate_total_with_empty_list()
    test_calculate_total_with_single_product()
    test_calculate_total_with_multiple_product()
    print("All tests passed!")
