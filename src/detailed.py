from datetime import datetime

def generate_froyo_receipt():
  # Copy the body of your generate_froyo_receipt() function from simple.py here!

#----------------------
# DO NOT MODIFY BELOW!
#----------------------

# Don't change these prices!
base_prices = {
  'small':  5.00,
  'medium': 7.00,
  'large':  9.00
}

# Don't change these prices!
topping_prices = {
  'peanuts': 0.50,
  'skittles': 0.75,
  'sprinkles': 0.25,
  'mochi': 1.00,
  'granola': 0.75,
}

def human_readable_time():
  return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def main():
  generate_froyo_receipt('Jill', 'small', base_prices['small'],
                         'vanilla',
                         peanuts=topping_prices['peanuts'], 
                         skittles=topping_prices['skittles'], 
                         sprinkles=topping_prices['sprinkles'],
                         mochi=topping_prices['mochi'])

  # No toppings please
  generate_froyo_receipt('Suresh', 'medium', base_prices['medium'], 'strawberry', order_type='Takeout')

  # This one's on the house to make up for the store's mistake
  generate_froyo_receipt('Max', 'large', 0, 
                         'chocolate', 'vanilla', 'blueberry',
                         order_type='Takeout',
                         granola=0,
                         skittles=0)

  # This one has an employee discount applied to it (get a medium for the price of small, and $0.25 toppings)
  generate_froyo_receipt('Zahara', 'medium', base_prices['small'],
                         'raspberry', 'Cookies & Cream',
                         peanuts=0.25,
                         mochi=0.25)

if __name__ == '__main__':
  main()
