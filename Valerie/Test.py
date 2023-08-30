import pytest
from Review import Review
from Restaurant import Restaurant
from Customer import Customer

# Review Tests
def test_review_creation():
    myreview = Review("Valerie Kandagor", "Sippin serenade", 19)
    assert myreview.customer == "Valerie Kandagor"
    assert myreview.restaurant == "Sippin serenade"
    assert myreview.rating == 19

def test_invalid_rating():
    with pytest.raises(ValueError):
        myreview = Review("Valerie Kandagor", "Sippin serenade", "invalid")

# Restaurant Tests
def test_restaurant_creation():
    myrestaurant = Restaurant("Sippin serenade")
    assert myrestaurant.name == "Sippin serenade"

# Customer Tests
def test_customer_creation():
    my_customer = Customer("Valerie", "Kandagor")
    assert my_customer.full_name == "Valerie Kandagor"

# Run tests
if __name__ == "__main__":
    pytest.main()
