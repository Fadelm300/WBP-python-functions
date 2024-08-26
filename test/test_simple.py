import unittest
from unittest.mock import patch

import sys

# So that `python test/test_simple.py` works
# and `python test_simple.py` works when in the 'test' directory
sys.path += ['src', '../src']

from simple import base_prices, generate_froyo_receipt

@patch('builtins.print')
class GenerateFroyoReceipt(unittest.TestCase):

  def _assert_output(self, mocked_print, expected_output):
    for i, line in enumerate(expected_output):
      if line:
        args = mocked_print.call_args_list[i][0]
        # sys.stdout.write(str(len(args)))
        # sys.stdout.write(' ')
        # sys.stdout.write(str(args))
        # sys.stdout.write('\n')
        # sys.stdout.write(' '.join(args))
        # sys.stdout.write('\n')
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
      r'Price: \$5.00',
      '-----------------------------------',
      None
    ]

    generate_froyo_receipt('Jill', 'small', base_prices['small'],
                           'vanilla',
                           'peanuts', 'skittles', 'sprinkles', 'mochi')

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

  def test_keywords_out_of_order(self, mocked_print):

    expected_output = [
      '-----------------------------------',
      'Dine In order for Keisha',
      '-----------------------------------',
      'small froyo: blueberry',
      None,
      r'Order Placed: \d\d\d\d-\d\d-\d\d \d\d:\d\d:\d\d',
      r'Price: \$5.00',
      '-----------------------------------',
      None
    ]

    generate_froyo_receipt('Keisha', base_price=base_prices['small'], size='small', flavor='blueberry')

    self._assert_output(mocked_print, expected_output)

  def test_on_the_house(self, mocked_print):

    expected_output = [
      '-----------------------------------',
      'Takeout order for Max',
      '-----------------------------------',
      'large froyo: chocolate',
      '- granola',
      '- skittles',
      None,
      r'Order Placed: \d\d\d\d-\d\d-\d\d \d\d:\d\d:\d\d',
      r'Price: \$0.00',
      '-----------------------------------',
      None
    ]

    generate_froyo_receipt('Max', 'large', 0, 'chocolate', 'granola', 'skittles', order_type='Takeout')

    self._assert_output(mocked_print, expected_output)

  def test_employee_discount(self, mocked_print):

    expected_output = [
      '-----------------------------------',
      'Dine In order for Zahara',
      '-----------------------------------',
      'medium froyo: raspberry',
      '- peanuts',
      '- mochi',
      None,
      r'Order Placed: \d\d\d\d-\d\d-\d\d \d\d:\d\d:\d\d',
      r'Price: \$5.00',
      '-----------------------------------',
    ]

    generate_froyo_receipt('Zahara', 'medium', base_prices['small'], 'raspberry',
                         'peanuts', 'mochi')

    self._assert_output(mocked_print, expected_output)

if __name__ == '__main__':
  unittest.main()
