# Drone Cones Low Level Design

## Django Server
POST Requests
* new user
    * server receives new user information to add to database
* new drone lender
    * server receives new drone lender info to add to database
* order info
    * server receives:
        * amount of ice cream ordered (and flavor)
        * amount of cones ordered (and type)
        * amount of toppings ordered (and type)
        * cost of the order
        * drone used
* update inventory



GET Requests
* available drones
    * server receives size of order and checks database for available drones of correct size
    * server sends availabe drones with their size
* available inventory
    * server sends:
        * options of cones available
        * options of ice cream available
        * options of toppings available
* correct password for login
    * server checks the login info against database
    * server sends on OK to continue or a NOT OK
* manager reports
    * server sends over past order data
    * server sends revenue data
    * server sends drone info

### psuedo code
```
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

## Order Page Psudeo-Code Design

The order page would contain:
*	dropdown list of the icecream cone flavors
*	dropdown list of the icecream flavors
*	a list of icecream toppings

```JavaScript
order = // List of Cones Object to return to the server

currCone = // new Cone object

options = //list of icecream flavors/cones (may have too add to the database)

toppings = //String list of toppings for the cone

iceTops = //list of ice cream toppings

// Select what ice cream flaver/cone you want as a select input <select> </select> from svelte
dropDownMenu(options) 

// Display list of toppings once the selected topping is choosen use group input from svelte to 
listOfToppings(iceTops)


//Once the options have been chosen there are going to be four buttons 


// a button stating the user is finished with the cone and this button will add the cone object to the orderlist, then update price in order
button("addToCart")

// This button would lead to a sub-page, to view order and the checkout button would be there
button("cart", order)

// This button would lead to a page, to view account page
button("account")

// This button would lead to a page, to view the contact page 
button("contact")

```

### Cart Page Psudeo-Code Design

This page would include:
*	a view list of the cone object in the order
*	a checkout button to finish order

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

### Manager Page Psudeo-Code Design

This page would include:
* graph/numerical of the quantity of inventory items 
* current revenue and expense
* List of contact objects and displays list

This will request data from database/library
* For the revenue and expense for the day
* Import chart.js call for graphing data


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


### Drone page Psudeo-Code Design

This page would include:
* The list of the operator drones
* add new drones with specs

```JavaScript
drones = // get the data from the database for drones list

// This will diplay a list of drones with Specs
// This will also display the drones status
// Each drone list would contain a remove button to remove the drone from their list
dronesList(drones)


//T his will display a dropdown menu list for drone type
droneType = // inputs may be small, medium, large

droneCapacity = // this will be a numeric input for weight capacity of the drones

// This button would post the new drone in the list for the drone operator
button("addDrones")
```
