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
Psuedo Code: To be completed
