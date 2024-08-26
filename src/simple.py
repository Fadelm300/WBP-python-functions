from datetime import datetime

def generate_froyo_receipt():
  print('-'*35)
  print()
  print('-'*35)

  print()


  print()

  print(f'Order Placed: {human_readable_time()}')
  print(f'Price: ${}') 
  print('-'*35)
  print()

#----------------------
# DO NOT MODIFY BELOW!
#----------------------

# Don't change these prices!
base_prices = {
  'small':  5.00,
  'medium': 7.00,
  'large':  9.00
}

def human_readable_time():
  return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def main():
  generate_froyo_receipt('Jill', 'small', base_prices['small'],
                         'vanilla',
                         'peanuts', 'skittles', 'sprinkles', 'mochi')

  # No toppings please
  generate_froyo_receipt('Suresh', 'medium', base_prices['medium'], 'strawberry', order_type='Takeout')

  # Using keyword arguments out of order
  generate_froyo_receipt('Keisha', base_price=base_prices['small'], size='small', flavor='blueberry')

  # This one's on the house to make up for the store's mistake
  generate_froyo_receipt('Max', 'large', 0, 'chocolate', 'granola', 'skittles', order_type='Takeout')

  # This one has an employee discount applied to it (get a medium for the price of small)
  generate_froyo_receipt('Zahara', 'medium', base_prices['small'], 'raspberry',
                         'peanuts', 'mochi')

if __name__ == '__main__':
  main()
