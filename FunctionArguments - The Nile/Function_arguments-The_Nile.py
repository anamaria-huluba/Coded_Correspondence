# LEARN INTERMEDIATE PYTHON 3

# Function Arguments - The Nile

# The Nile fullfilment agency brings everything you could possibly want straight to your door! Use your knowledge of Python functions and how to manipulate arguments to help automate practices for the biggest world-changing company.

from nile import get_distance, format_price, SHIPPING_PRICES
from test import test_function

# Define calculate_shipping_cost() here:
def calculate_shipping_cost(from_coords, to_coords, shipping_type = 'Overnight'):
  distance = get_distance(*from_coords, *to_coords)
  shipping_rate = SHIPPING_PRICES[shipping_type]
  price = distance * shipping_rate
  return format_price(price)

# Test the function by calling 
test_function(calculate_shipping_cost)

# Define calculate_driver_cost() here
def calculate_driver_cost(distance, *drivers):
  cheapest_driver = None
  cheapest_driver_price = None
  for driver in drivers:
    driver_time = driver.speed * distance
    price_for_driver = driver.salary * driver_time
    if cheapest_driver is None:
      cheapest_driver = driver 
      cheapest_driver_price = price_for_driver
    elif price_for_driver < cheapest_driver_price:
      cheapest_driver = driver 
      cheapest_driver_price = price_for_driver
  return cheapest_driver_price, cheapest_driver

# Test the function by calling 
test_function(calculate_driver_cost)

# Define calculate_money_made() here
def calculate_money_made(**trips):
  total_money_made = 0
  for trip_id, trip in trips.items():
    trip_revenue = trip.cost - trip.driver.cost
    total_money_made  += trip_revenue
  return total_money_made

# Test the function by calling 
test_function(calculate_money_made)

# Outputs:
# OK! calculate_shipping_cost() passes tests
# OK! calculate_driver_cost() passes tests
# OK! calculate_money_made() passes tests

# FUNCTION ARGUMENTS
# Review
# I learned all about how functions can accept different arguments and different styles in which we can pass those arguments in. 

#I learned:
# How to pack positional arguments in a function with *args.
# How to work with *args using iteration and other positional arguments.
# How to pack keyword arguments in a function with **kwargs.
# How to work with **kwargs using iteration and other keyword arguments.
# How to combine all different types of arguments to gain the most flexibility in our function declarations.
# How to use an unpacking operator (* or **) to unpack arguments in a function call.
# How to use an unpacking operator (* or **) on iterables.