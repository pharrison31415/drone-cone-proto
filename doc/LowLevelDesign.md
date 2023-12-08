# Drone Cones Low Level Design

## Introduction

This document will outline the low level design of the Drone Cones App.
Here, we talk about the types of functions needed in both the front end and the back end.
We also outline what we want the basic structure of the app to look like using wire frame.

## Table of Contents

- [Django Server](#django-server)
- [Database](#database)
- [Front End Views](#front-end-views)
- [Front End Logic](#front-end-logic)

## Django Server

The Django server will use POST, GET, PATCH, and DELETE requests as access points for the data base.

Outlines of each of the endpoints can be found in the [API Documentation](../apps/api/api-documentation.md)

### pseudo code

```python
def receive_requests(request)
   if request.method == POST
      data = {
         'type': "post",
         'data': request.POST
      }
   elif request.method == GET
      data = {
         'type: "get",
         'data': request.GET
      }
   return JsonResponse(data)

def handle_data(data)
   if type == POST
      give data to the database
   elif type == GET
      return the requested data from the database
```

### API Security

When making any API requests for private information there is a token associated with who has access that must be given in order for a response to be returned to the client. These tokens are the following:

- Customer Token
- Manager Token
- Owner Token

When attempting to access or update any personal customer information the customer token must be verified. When attempting to access business related information such as total inventory, revenue, and price information the manager token must be verified. And when attemptin to access personal drone information the owner token must be verified.

### Password Security

Passwords will be stored and kept secure using the Django automatic hashing function. Not even managers viewing their customers will be able to view what the passwords are. When a customer views their profile their password will not show up. Currently, there is no way to recover their password, this may cause some inconvenience but will help protect customer privacy at this prototype level.

## Database

Our database will use SQLite.
We will have some default data that will need to be filled.
Here, we outline what data is needed in the default migrations and what our database objects will look like and contain.

### Migrations

- Fill DroneType with three drone types:

  1. Light with capacity 1
  2. Medium with capacity 4
  3. Heavy with capacity 8

- Fill ConeType with two cone types (with their respective details):

  1. Cake
  2. Waffle

- Fill IceCreamType with three ice cream types (with their respective details):

  1. Vanilla
  2. Chocolate
  3. Strawberry

- Fill ToppingType with three topping types (with their respective details):
  1. Sprinkles
  2. Cherry
  3. Chocolate sauce

### Pseudo-schema

Here is a pseudo-schema for the data base.
This includes the different objects that will be used to keep information organized.

[pseudo-schema.txt](./pseudo-schema.txt)

## Front End Views

Here are mockups of what the application will look like.

- [Log-in page](https://wireframe.cc/F08gdT)
- [Order page](https://wireframe.cc/fHa6vd)
- [Cart page](https://wireframe.cc/yUR5pU)
- [Account page](https://wireframe.cc/aqI5bl)
- [Oder tracking page](https://wireframe.cc/rMDQMf)
- [Contact/Report Page](https://wireframe.cc/IdDwLg)

## Front End Logic

### Order Page Pseudo-Code Design

The order page would contain:

- dropdown list of the ice cream cone flavors
- dropdown list of the ice cream flavors
- a list of ice cream toppings

```JavaScript
order = // List of Cones Object to return to the server

currCone = // new Cone object

options = //list of ice cream flavors/cones (may have too add to the database)

toppings = //String list of toppings for the cone

iceTops = //list of ice cream toppings

// Select what ice cream flavor/cone you want as a select input <select> </select> from svelte
dropDownMenu(options)

// Display list of toppings once the selected topping is chosen use group input from svelte to
listOfToppings(iceTops)


//Once the options have been chosen there are going to be four buttons


// a button stating the user is finished with the cone and this button will add the cone object to the order list, then update price in order
button("addToCart")

// This button would lead to a sub-page, to view order and the checkout button would be there
button("cart", order)

// This button would lead to a page, to view account page
button("account")

// This button would lead to a page, to view the contact page
button("contact")

```

### Cart Page Pseudo-Code Design

This page would include:

- a view list of the cone object in the order
- a checkout button to finish order

```JavaScript
order = //Pass the order list from previous page

// This function would display a list of cones from the order
// Next to each cone order there is going to be a remove button to remove a cone from list
// Also have a quantity dropdown to update the amount of same cone the user would like to add
listOfCones(order)

// This button states the customer is done with the order
// This will send the order object to the company servers to assign a drone operator to complete the order
// Update revenue and inventory data from the database
button("Checkout", order)

// This button will return to the order page with the current order object
button("Order", order)

// Note: This page will also contain the the account button and the contact button

```

### Manager Page Pseudo-Code Design

This page would include:

- graph/numerical of the quantity of inventory items
- current revenue and expense
- List of contact objects and displays list

This will request data from database/library:

- For the revenue and expense for the day
- Import chart.js call for graphing data

```JavaScript
/*
For this page to work it would need to get information from the database to get data for revenue
This will import the library chart.js in order to graph the data giving
*/

data = //get data from the database for revenue and expense

//Uses the data to graph line
var chart = new chartjs(....)

/*
Note: This will Displays the revenue at the center of the page
also if the border is green expense are below revenue and vice versa when red
*/

inventory = //get data object inventory from database

// This will display the inventory amount for each flavor, cone, topping
// This will also change the background red when a inventory item reach a low number
inventoryDisplay(inventory)

contact = //get data from database for customers trying to contact

// Display a scroll list of contacts with a checkmark next to contact if contact has been handled
// Once contacted and handled the user will be able to post the contact to handled: True
listOfContact(contacts)
```

### Drone page Pseudo-Code Design

This page would include:

- The list of the operator drones
- add new drones with specs

```JavaScript
drones = // get the data from the database for drones list

// This will display a list of drones with Specs
// This will also display the drones status
// Each drone list would contain a remove button to remove the drone from their list
dronesList(drones)


//T his will display a dropdown menu list for drone type
droneType = // inputs may be small, medium, large

droneCapacity = // this will be a numeric input for weight capacity of the drones

// This button would post the new drone in the list for the drone operator
button("addDrones")
```

### Track Order page Pseudo-Code Design

This page would include:

- The details of an order such as:
  - time placed
  - cone ordered
  - time left to devilery/ time delivered
  - order number
  - cost

```JavaScript
order = // get the data from the database from order list

// This will display the order details
orderDisplay(order)
```

### Contact Page Pseudo-Code Design

This page would include:

- a text entry for name, email, and message with a submit button

```JavaScript
// This will send a message to the managers
sendMessage()
```

### Log in Page Pseudo-Code Design

This page would let the user log in

- it would need to be able to check if
  - the username exists
  - password exists

```JavaScript
// This will get the username and password that was entered and check to see if they match eachother and if they do let them log in going to the account page first
login(username, password)
```

### Account Page Pseudo-Code Design

This page would include:

- The account name
- recent orders
  - order details
- address

```JavaScript
recentOrders = // get the recent orders from the database
account = // get account from database

// this will display the order details
// each will have an add to cart button and be able to click on it to see more details, go to order detail page for that order
for each order in RecentOrders {
  orderDisplay(order)
}
```

### Sign-Up Page Pseudo-Code Design

This page would have to post to the database:

- username
- password
- role

```JavaScript
// This will add the user to the database with the correct role
addUser(username, password, role)
```

### Front Page Pseudo-Code Design

This page will ask to log in or sign up

```JavaScript
// This will lead the user to the log in page
button('login', login)
// This will lead the user to the sign up page
button('sign up', signUp)
```
