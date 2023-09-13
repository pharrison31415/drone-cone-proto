# Drone Cones Requirements Specifications - Reworded

- The system shall display a home screen with five different options: Sign up(customer), Sign up(drone operator), Log in, Guest Checkout, Contact
## Sign Up (Customer)
- The system shall request the users full name, a username, and a password
- The system shall store the information to the database to create the account when "Submit" button is pressed
- The system shall then direct the user to the log in page
## Sign Up (Drone Operator)
- The system shall request the full name, username, and password of the user
- The system shall store information to the database when "Submit" is pressed
- The system shall then direct the user to the log in page
## Log In
- The System shall request the username and password
- The system shall check the database against the given information
- The system shall display the main page of a logged in user
## Main Page (Drone Operator Logged in)
- The system shall display an option to add a drone
  - The system shall request the name, size, and availability of the drone
  - The system shall request the user to check a box and accept the terms and conditions
-  The system shall display current drones and status of if they are currently fulfilling an order or not
## Main Page (Customer Logged in)
- The system shall display the company logo and an option to place an order
  - The system shall allow the customer to choose from at least 3 different ice cream cones
  - The system shall allow the customer to choose from at least 3 different ice cream flavors
  - The system shall allow the customer to choose to add toppings from a list of at least 3 different toppings
  - The system shall allow the customer to add the completed ice cream cone to cart
  - The system shall display the options to add another cone to the order or to checkout
## CheckOut
- The system shall display the different cones that have been added to the cart (including prices)
- The system shall request a delivery address
- The system shall display the total cost
- The system shall ask for payment information
- The system shall display a "Complete Purchase" button
## Complete Purchase - Track Order
- The system shall file the order information into the database and begin timer
- The system shall display a timer for when the ice cream will arrive
## Contact Page
- The system shall request information from the user:
  - Name
  - Email/Phone Number
  - Comment/Question
- When "submit" button is pressed the system shall save the form to the database
