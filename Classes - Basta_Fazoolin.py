# LEARN PYTHON 3
# Classes-Basta Fazoolin

# You’ve started position as the lead programmer for the family-style Italian restaurant Basta Fazoolin’ 
# with My Heart. The restaurant has been doing fantastically and seen a lot of growth lately. You’ve been 
#  to keep things organized.

# 1. At Basta Fazoolin’ with my Heart our motto is simple: when you’re here with family, that’s great! 
# We have four different menus: brunch, early-bird, dinner, and kids.
# Create a Menu class.
# 2. Give Menu a constructor with the five parameters self, name, items, start_time, and end_time.
# 3. Let’s create our first menu: brunch. Brunch is served from 11am to 4pm. The following items are sold during brunch:
# {
#   'pancakes': 7.50, 'waffles': 9.00, 'burger': 11.00, 'home fries': 4.50, 'coffee': 1.50, 'espresso': 3.00, 'tea': 1.00, 'mimosa': 10.50, 'orange juice': 3.50
# }

class Menu:
  def __init__(self, name, items, start_time, end_time):
    self.name = name
    self.items = items
    self.start_time = start_time
    self.end_time = end_time

# Brunch Menu:

brunch_items = {
  'pancakes': 7.50, 'waffles': 9.00, 'burger': 11.00, 'home fries': 4.50, 'coffee': 1.50, 'espresso': 3.00, 'tea': 1.00, 'mimosa': 10.50, 'orange juice': 3.50
}
brunch_menu = Menu("Brunch", brunch_items, 1100, 1600)

print(brunch_menu.name)

# 4. Let’s create our second menu item early_bird. Early-bird Dinners are served from 3pm to 6pm. The following items are available during the early-bird menu:

# {
#   'salumeria plate': 8.00, 'salad and breadsticks (serves 2, no refills)': 14.00, 'pizza with quattro formaggi': 9.00, 'duck ragu': 17.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 1.50, 'espresso': 3.00,
# }

# Early_bird Menu:

early_bird_items = {
  'salumeria plate': 8.00, 'salad and breadsticks (serves 2, no refills)': 14.00, 'pizza with quattro formaggi': 9.00, 'duck ragu': 17.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 1.50, 'espresso': 3.00,
}
early_bird_menu = Menu("Early-bird Dinners", early_bird_items, 1500, 1800)

# 5. Let’s create our third menu, dinner. Dinner is served from 5pm to 11pm. The following items are available for dinner:

# {
#   'crostini with eggplant caponata': 13.00, 'ceaser salad': 16.00, 'pizza with quattro formaggi': 11.00, 'duck ragu': 19.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 2.00, 'espresso': 3.00,
# }

# Dinner Menu:

dinner_items = {
  'crostini with eggplant caponata': 13.00, 'ceaser salad': 16.00, 'pizza with quattro formaggi': 11.00, 'duck ragu': 19.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 2.00, 'espresso': 3.00,
}
dinner_menu = Menu("Dinner", dinner_items, 1700, 2300)

# 6. And let’s create our last menu, kids. The kids menu is available from 11am until 9pm. The following items are available on the kids menu.

# {
#   'chicken nuggets': 6.50, 'fusilli with wild mushrooms': 12.00, 'apple juice': 3.00
# }

# Kids Menu
kids_items = {
  'chicken nuggets': 6.50, 'fusilli with wild mushrooms': 12.00, 'apple juice': 3.00
}

kids_menu = Menu("Kids", kids_items, 1100, 2100)

print(kids_menu)
# returns: <__main__.Menu object at 0x7f03131a1860>
#It returns our object Menu and where it was stored, and this information is not very useful.


# 7. Give our Menu class a string representation method that will tell you the name of the menu. Also, 
# indicate in this representation when the menu is available.
# 8. Try out our string representation. If you call print(brunch) it should print out something like the following:
# brunch menu available from 11am to 4pm

class Menu:
  def __init__(self, name, items, start_time, end_time):
    self.name = name
    self.items = items
    self.start_time = start_time
    self.end_time = end_time

  def __repr__(self):
      return self.name + " menu available from " + str(self.start_time) + " to " + str(self.end_time)

print(kids_menu)
#returns: 
# Kids menu available from 1100 to 2100
#which gives us a lot more uesful information about our object.

# 9. Give Menu a method .calculate_bill() that has two parameters: self, and purchased_items, a list of the names 
# of purchased items.
# Have calculate_bill return the total price of a purchase consisiting of all the items in purchased_items.

class Menu:
  def __init__(self, name, items, start_time, end_time):
    self.name = name
    self.items = items
    self.start_time = start_time
    self.end_time = end_time
    
  def __repr__(self):
    return self.name + " menu available from " + str(self.start_time) + " to " + str(self.end_time)
    
  def calculate_bill(self, purchased_items):
    bill = 0
    for purchased_item in purchased_items:
      if purchased_item in self.items:
        bill += self.items[purchased_item]
    return bill

# 10. Test out Menu.calculate_bill(). We have a breakfast order for one order of pancakes, one order of home fries, and one coffee. 
# Pass that into brunch.calculate_bill() and print out the price.

print(brunch_menu.calculate_bill['pancakes', 'home fires', 'coffee'])

# 11. What about an early-bird purchase? Our last guests ordered the salumeria plate and the vegan 
# mushroom ravioli. Calculate the bill with .calculate_bill().

print(early_bird_menu.calculate_bill['salumeria plate', 'mushroom ravioli (vegan)'])

# Creating the Franchises

# 12. Basta Fazoolin’ with my Heart has seen tremendous success with the family market, which is 
# fantastic because when you’re at Basta Fazoolin’ with my Heart with family, that’s great!
# We’ve decided to create more than one restaurant to offer our fantastic menus, services, and ambience
# around the country.

# First, let’s create a Franchise class.

# 13. Give the Franchise class a constructor. Take in an address, and assign it to self.address. 
# Also take in a list of menus and assign it to self.menus.

class Franchise:
  def __init__(self, address, menus):
    self.address = address
    self.menus = menus

# 14. Let’s create our first two franchises! Our flagship store is located at "1232 West End Road" 
# and our new installment is located at "12 East Mulberry Street". 
# Pass in all four menus along with these addresses to define flagship_store and new_installment.

class Franchise:
  def __init__(self, address, menus):
    self.address = address
    self.menus = menus

menus = [brunch_menu, early_bird_menu, dinner_menu, kids_menu]

flagship_store = Franchise('1232 West End Road', menus)
new_installment = Franchise('12 East Mulberry Street', menus)

# 15. Give our Franchises a string representation so that we’ll be able to tell them apart. If we print out a 
# Franchise it should tell us the address of the restaurant.

class Franchise:
  def __init__(self, address, menus):
    self.address = address
    self.menus = menus
  def __repr__(self):
    return self.address

#to test print(flagship_store)
#returns: 1232 West End Road

# 16. Let’s tell our customers what they can order! Give Franchise an .available_menus() method that takes in a time 
# parameter and returns a list of the Menu objects that are available at that time.

class Franchise:
  def __init__(self, address, menus):
    self.address = address
    self.menus = menus
  def __repr__(self):
    return self.address
  def available_menus(self, time):
    available_menus = []
    for menu in self.menus:
      if time >= menu.start_time <= menu.end_time:
        available_menus.append(menu)
    return available_menus

#17. Let’s test out our .available_menus() method! Call it with 12 noon as an argument and print out the results.

print(flagship_store.available_menus(1200))
# returns: [Brunch menu available from 1100 to 1600, Kids menu available from 1100 to 2100]

#18. Let’s do another test! See what is printed if we call .available_menus() with 5pm as an argument and print out the results.

print(new_installment.available_menus(1700))
#returns: [Brunch menu available from 1100 to 1600, 
# Early-bird Dinners menu available from 1500 to 1800, 
# Dinner menu available from 1700 to 2300, 
# Kids menu available from 1100 to 2100]

# 19. Since we’ve been so successful building out a branded chain of restaurants, we’ve decided to diversify. We’re going to create a restaurant that sells arepas!

# First let’s define a Business class.

#20. Give Business a constructor. A Business needs a name and a list of franchises.

class Business:
  def __init__(self, name, franchises):
    self.name = name
    self.franchises = franchises

# 21. Let’s create our first Business. The name is "Basta Fazoolin' with my Heart" and the two franchises are flagship_store and 
# new_installment.

basta = Business("Basta Fazoolin' with my Heart", [flagship_store, new_installment])

# 22. Before we create our new business, we’ll need a Franchise and before our Franchise we’ll need a menu. The items for our Take a’ Arepa available from 10am until 8pm are the following:

# {
#   'arepa pabellon': 7.00, 'pernil arepa': 8.50, 'guayanes arepa': 8.00, 'jamon arepa': 7.50
# }
# Save this to a variable called arepas_menu.

arepa_items = {
  'arepa pabellon': 7.00, 'pernil arepa': 8.50, 'guayanes arepa': 8.00, 'jamon arepa': 7.50
}
arepa_menu = Menu("Take a’ Arepa", arepa_items, 1000, 2000)

# 23.
# Next let’s create our first Take a’ Arepa franchise! Our new restaurant is located at "189 Fitzgerald Avenue". 
# Save the Franchise object to a variable called arepas_place.

arepas_place = Franchise("Take a’ Arepa", [arepa_menu])

24. #Now let’s make our new Business! The business is called "Take a' Arepa"!

arepa = Business("Take a’ Arepa", [arepas_place])

# 25. Congrats! You created a system of classes that help structure your code and perform all business requirements you need. 
# Whenever we need a new feature we’ll have the well-organized code required to make developing and shipping it easy.

print(arepa.franchises[0].menus[0])
#returns: Take a’ Arepa menu available from 1000 to 2000
