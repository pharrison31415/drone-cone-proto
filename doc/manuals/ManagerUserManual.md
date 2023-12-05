# Manager User Manual

## Introduction

This is the user manual for a manager on the Drone Cones website. If you have any questions, please follow the instructions below. These instructions will guide you through managing inventory, monitoring revenue, and reading customer messages.

## Inventory

The inventory is made up into three section. First the inventory, the purchases of the inventory, and the price update.

### Inventory - Stock

* This section displays the all the items in the company inventory. The "Unit Price:" is the price amount to buy for one unit for that item. The "quantity" is the amount of units the company have in stored.

### Purchase

This section is to buy more items for the inventory. Here are the instruction to use it.

1. Select the item type - This means to select a type of item for example: (Cones is for cone-types)
  1.1 By selecting the item type - It will give you a list of items in that item type.
2. Next Select an item - This means to select an item for that item type for example: (Cone contains Waffle and Cake items)
3. Enter the amount - This means to enter a number value to add the quantity amount of the item you selected.
4. Lastly hit purchase to purchase items

* `name`: name of the item being purchased
* `itemType`: is the type of the item being purchased: `coneType`, `iceCreamType`, or `toppingType`
* `additionalUnits`: positive integer of number of units to add to the inventory

*Note: no item will be purchase if one of the inputs are missing or is incorrect*

### Update Prices

This section is to update the prices on the inventory section

1. Select the item type - This means to select a type of item for example: (Cones is for cone-types)
2. Next under `unit cost` enter the new amount
3. Lastly hit the update button to update

* `itemType` (string telling if it is a cone, ice cream, or topping)
  * options are `coneType`, `iceCreamType`, or `toppingType`
* `unitCost` (positive integer. the new unit cost for the item in pennies)

*Note: no item will be purchase if one of the inputs are missing or is incorrect*

## Revenue

This section displays a graph of the revenue current as of the day. As well as the `revenue` and the `cost` of the item and lastly the total of the two as the `Net`

## Customer Contacts

This section displays the customer trying to contact the company. This will display the customer information and a check to if they were responded to. It is the manager duty to email back to the customer and mark it as responded, once the conflict has been resolve
