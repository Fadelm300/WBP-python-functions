# Python Functions
![Scenario](./assets/banner-scenario.png)

The company you work at writes custom receipt generation software, and you've been hired to write a receipt generator for a Frozen Yogurt chain!

Your job is to generate receipts for frozen yogurt orders. The information shown on the receipt can change depending on many factors like the size of the yogurts, the toppings ordered, whether it's Takeout or Dine In, etc.

---
![Requirements](./assets/banner-requirements.png)

- Understanding of Python functions
- Positional arguments
- Keyword arguments
- The use of `*args`
- The use of `**kwargs`

---
![Coding Practice](./assets/banner-coding.png)

### Preparation Steps

- Fork and clone this repository
- Navigate (`cd`) into the repository folder in your console
- Open up the repository folder in your code editor
  - If you're using Visual Studio Code, the command is `code .`

<br>

---

<br>

### Step 1

- Open up `src/simple.py`
- Read through the existing code.
- Make sure you understand what each line of the `main()` function does. It is the guide to your success in completing this exercise.
- Carefully analyze each call of `generate_froyo_receipt()` to infer what the intended functionality should be.

<br>

Your job is to write the `generate_froyo_receipt()` function. You'll have to determine how many, and what kind of parameters need to be accepted by the function. You'll also need to implement the body of the function to generate proper receipts for each order.
<br>  
Note: Some small bits of it have already been written for you. Do not modify any of the code where it says not to!

The customer has requested that the receipt generated must show:
  - The customer's name
  - The size of the yogurt they want: `small`, `medium`, or `large`
  - The flavor of the frozen yogurt they have chosen (only one flavor allowed)
  - All the toppings they've requested (all toppings are free!)
  - When the order was placed
  - Whether it was Dine In or Takeout
  - And the price of the order (which can be customizable so that free or discounted yogurts can be given)
- The expected output, when you are successful, will be the following. Each receipt corresponds to one function call in `main()`:

  ```
  -----------------------------------
  Dine In order for Jill
  -----------------------------------
  small froyo: vanilla
  - peanuts
  - skittles
  - sprinkles
  - mochi

  Order Placed: 2023-04-09 15:47:45
  Price: $5.00
  -----------------------------------

  -----------------------------------
  Takeout order for Suresh
  -----------------------------------
  medium froyo: strawberry

  Order Placed: 2023-04-09 15:47:45
  Price: $7.00
  -----------------------------------

  -----------------------------------
  Dine In order for Keisha
  -----------------------------------
  small froyo: blueberry

  Order Placed: 2023-04-09 15:47:45
  Price: $5.00
  -----------------------------------

  -----------------------------------
  Takeout order for Max
  -----------------------------------
  large froyo: chocolate
  - granola
  - skittles

  Order Placed: 2023-04-09 15:47:45
  Price: $0.00
  -----------------------------------

  -----------------------------------
  Dine In order for Zahara
  -----------------------------------
  medium froyo: raspberry
  - peanuts
  - mochi

  Order Placed: 2023-04-09 15:47:45
  Price: $5.00
  -----------------------------------
  ```

- To check that you wrote up `src/simple.py` correctly:
  - Run `python test/test_simple.py`
  - You should see:
  ```
  % python test/test_simple.py
  .....
  ----------------------------------------------------------------------
  Ran 5 tests in 0.002s

  OK
  ```

<br>

---

<br>

### Step 2:

The froyo chain has decided to change its business model! It won't be popular with the customers, but inflation has forced the company to charge for each topping separately. However, the chain will now allow each order to include multiple flavors, which is great!

- Open up `src/detailed.py`
- Read it and understand it
- This is a little different from the "simple" receipts from Step 1
- Analyze carefully each function call in `main()` to understand how it's changed, with the ability now to specify multiple flavors and multiple toppings

Your job once again is to write the `generate_froyo_receipt()` function. You'll have to determine how many, and what kind of parameters need to be accepted by the function. You'll also need to implement the body of the function to generate proper receipts for each order.
  - Copy over the body from your previously completed `src/simple.py` and start from there.
  - Do not modify any of the code where it says not to!

The customer has requested that the receipt generated must show:
  - The customer's name
  - The size of the yogurt they want: `small`, `medium`, or `large`
  - The flavor of the frozen yogurt they have chosen (you can specify multiple flavors now!)
  - All the toppings they've requested
  - When the order was placed
  - Whether it was Dine In or Takeout
  - And the total price of the order
    - The base price depending on size is customizable when the function is called
    - The price of each topping is also customizable!
- The expected output, when you are successful, will be the following. Each receipt corresponds to one function call in `main()`:

  ```
  -----------------------------------
  Dine In order for Jill
  -----------------------------------
  small froyo: vanilla
  - peanuts
  - skittles
  - sprinkles
  - mochi

  Order Placed: 2023-04-09 16:00:37
  Price: $7.50
  -----------------------------------

  -----------------------------------
  Takeout order for Suresh
  -----------------------------------
  medium froyo: strawberry

  Order Placed: 2023-04-09 16:00:37
  Price: $7.00
  -----------------------------------

  -----------------------------------
  Takeout order for Max
  -----------------------------------
  large froyo: chocolate / vanilla / blueberry
  - granola
  - skittles

  Order Placed: 2023-04-09 16:00:37
  Price: $0.00
  -----------------------------------

  -----------------------------------
  Dine In order for Zahara
  -----------------------------------
  medium froyo: raspberry / Cookies & Cream
  - peanuts
  - mochi

  Order Placed: 2023-04-09 16:00:37
  Price: $5.50
  -----------------------------------
  ```

- To check that you wrote up `src/detailed.py` correctly:
  - Run `python test/test_detailed.py`
  - You should see:
  ```
  % python test/test_detailed.py
  ....
  ----------------------------------------------------------------------
  Ran 4 tests in 0.002s

  OK
  ```
--- 

### Testing

- To check that you did everything right, you should run all the tests together:
  - Run `python -m unittest`
  - You should see:
  ```
  % python -m unittest
  .........
  ----------------------------------------------------------------------
  Ran 9 tests in 0.003s

  OK
  ```
