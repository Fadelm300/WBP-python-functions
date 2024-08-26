import unittest
from unittest.mock import patch

import sys

# So that `python test/test_detailed.py` works
# and `python test_detailed.py` works when in the 'test' directory
sys.path += ['src', '../src']

from detailed import base_prices, topping_prices, generate_froyo_receipt

@patch('builtins.print')
class GenerateFroyoReceipt(unittest.TestCase):

  def _assert_output(self, mocked_print, expected_output):
    for i, line in enumerate(expected_output):
      if line:
        args = mocked_print.call_args_list[i][0]
        self.assertRegex(' '.join(args), line)

  def test_basic_call(self, mocked_print):

    expected_output = [
      '-----------------------------------',
      'Dine In order for Jill',
      '-----------------------------------',
      'small froyo: vanilla',
      '- peanuts',
      '- skittles',
      '- sprinkles',
      '- mochi',
      None,
      r'Order Placed: \d\d\d\d-\d\d-\d\d \d\d:\d\d:\d\d', # 'Order Placed: YYYY-MM-DD hh:mm:ss',
      r'Price: \$7.50',
      '-----------------------------------',
      None
    ]

    generate_froyo_receipt('Jill', 'small', base_prices['small'],
                           'vanilla',
                           peanuts=topping_prices['peanuts'], 
                           skittles=topping_prices['skittles'], 
                           sprinkles=topping_prices['sprinkles'],
                           mochi=topping_prices['mochi'])

    self._assert_output(mocked_print, expected_output)

  def test_no_toppings(self, mocked_print):

    expected_output = [
      '-----------------------------------',
      'Takeout order for Suresh',
      '-----------------------------------',
      'medium froyo: strawberry',
      None,
      r'Order Placed: \d\d\d\d-\d\d-\d\d \d\d:\d\d:\d\d',
      r'Price: \$7.00',
      '-----------------------------------',
      None
    ]

    generate_froyo_receipt('Suresh', 'medium', base_prices['medium'], 'strawberry', order_type='Takeout')

    self._assert_output(mocked_print, expected_output)

  def test_on_the_house(self, mocked_print):

    expected_output = [
      '-----------------------------------',
      'Takeout order for Max',
      '-----------------------------------',
      'large froyo: chocolate / vanilla / blueberry',
      '- granola',
      '- skittles',
      None,
      r'Order Placed: \d\d\d\d-\d\d-\d\d \d\d:\d\d:\d\d',
      r'Price: \$0.00',
      '-----------------------------------',
      None
    ]

    generate_froyo_receipt('Max', 'large', 0, 
                           'chocolate', 'vanilla', 'blueberry',
                           order_type='Takeout',
                           granola=0,
                           skittles=0)

    self._assert_output(mocked_print, expected_output)

  def test_employee_discount(self, mocked_print):

    expected_output = [
      '-----------------------------------',
      'Dine In order for Zahara',
      '-----------------------------------',
      'medium froyo: raspberry / Cookies & Cream',
      '- peanuts',
      '- mochi',
      None,
      r'Order Placed: \d\d\d\d-\d\d-\d\d \d\d:\d\d:\d\d',
      r'Price: \$5.50',
      '-----------------------------------',
    ]

    generate_froyo_receipt('Zahara', 'medium', base_prices['small'],
                           'raspberry', 'Cookies & Cream',
                           peanuts=0.25,
                           mochi=0.25)

    self._assert_output(mocked_print, expected_output)

if __name__ == '__main__':
  unittest.main()
