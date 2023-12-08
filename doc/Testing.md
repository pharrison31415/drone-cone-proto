# Testing

## Introduction

As all of our codebase's functionality was database dependent, it was difficult to write unit tests to check the state of the data. Instead, we did thorough manual testing to ensure the application was running smoothly and without certain anticipated errors.

These are the things we did when testing the website. We did this while implementing new features to make sure nothing broke. We also did a final check doing these same things

## Tests

### Test as a User

- Order as guest from home screen

  - Add cone to cart
    - Does not add when cone needs input
  - Add multiple cones to cart
    - Can scroll on
  - Delete a cone from the cart
  - Order does not continue if we need more info
    - Address
    - Payment
    - Cart with at least 1 cone
  - Order places properly
  - Tracks the order

- Home screen to sign up

  - Can create a new account
    - After creation should tell us to sign in

- Home screen to sign in

  - Can sign into new account
    - Cookie put on the device

- Adding an address

  - Can add an address
  - Can delete an address

- Try and place an order with an account
  - Add cone to cart
    - Does not add when cone needs input
  - Add multiple cones to cart
    - Can scroll on
  - Delete a cone from the cart
  - Order does not continue if we need more info
    - Address
    - Payment
    - Cart with at least 1 cone
  - Order places properly
  - Tracks the order
  - Should put an order in order history
    - Check price
    - Check cone amount
    - Check status

### Test as drone owner

- After placing an order, is an drone marked as delivering

  - Can not deactivate drone when delivering

- Can Edit Drone

  - Change name
  - Change size

- Can add a drone

- Can set drone to activate/de-active

- Drone should have income after order is complete

### Test as a manager

- Can see inventory
- Can re-supply
- Can see the graphs of revenue
