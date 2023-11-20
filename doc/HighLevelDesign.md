# High Level Design Document

## Introduction

Drone Cones will be a web app that anyone can use on any of their devices that can run a web browser. This means that our customers will be able to order a cone from their phone, or from their personal computer. We will be using Django for the backend, which will help the developers create an API that is easy to use and maintain. Drone cones will be using Svelte for the front end. Svelte is cutting edge, and will allow us to create UI that looks and feels really clean for the user. We will run a 2-tier architecture so we can access the database from multiple points at the same time. The Web Application will be easy to use and will make customers want to use Drone Cones again whenever they need a tasty treat.

## Table of Contents

- [Django - Backend Development](#django---backend-development)
- [Svelte - Frontend Development](#svelte---frontend-development)
- [Architecture](#architecture)
- [Web App Functionality](#website-application)
- [UML Diagram](#uml-diagram)

## Frameworks and Programming Languages

### Django - Backend Development

The system logic and backend development will be implemented on the Django Framework. Django is a python based web development framework designed to help web developers develop their applications as smoothly as possible by providing the base requirements need for a web app. This framework provides simpler implementation of views, templates, and databases. Django provides compatibility with several different types of databases. This allows web developers to be able to choose based on their own abilities and what individual projects require. Django also provides API abilities which allows for easier integration with other frameworks and programs.

The design of the Django framework is ideal for the Drone Cones backend system for the following reasons:

- Choose a database (SQLite) that is easy to work with and effectively stores necessary data
- Use a high level language that provides smooth transitioning from design to implementation
- Use relevant and well known framework and language that will be easier to train new people on as the application grows
- Use API capabilities to connect with front end framework for smooth communication of information between the server and the user

### Svelte - Frontend Development

The frontend and the visuals will be implemented on a Svelte framework. Svelte is a reactive UI framework. Svelte is a javascript based web development framework designed to help with HTML, CSS, JavaScript, and UI that would react to changes in the data. This framework provides no virtual DOM, providing reconcile changes and update the actual DOM. It updates the elements directly as the data changes, which results in faster updates and less memory overhead. Svelte also provides scoped styling to help prevent unintentional style conflicts. Svelte also provides HTML, CSS and JavaScript integrations, letting you write component templates in HTML, styles in CSS, and logic in JavaScript. Svelte also has animation support to easily create smooth transitions and animations within. Svelte makes it straightforward to handle form inputs, events, and user interactions, simplifying common tasks like form validation and event handling.

The design of the Svelte framework is ideal for the Drone Cones frontend system for the following reasons:

- A highly optimized JavaScript during build time.
- Small bundle sizes, Svelte generates smaller JavaScript bundles.
- Simplicity, Svelte's syntax and approach is relatively simple and easy to learn.
- Reactivity to data changes to the backend.
- No runtime framework overhead, code is as close to native JavaScript as possible.
- Small bundle sizes make it well-suited for building mobile-responsive websites that perform well on a variety if devices.

### Architecture

The system's architecture will be a 2-tier Client/Server Architecture. This means that the information the application will need will be accessed through protocol.

Using a 2-tier client/server architecture is ideal for Drone Cones for the following reasons:

- Establish a secure way to transfer data between client and server
- Protocol tightly joins client with server, so when server is being updated, client is being changed to match
- The application can be run on multiple computers without having to scale the servers as much
  - Amount of clients per server is not 1:1
- Implementation of a 2-tier Client/Server Architecture will allow us to properly scale once we are done prototyping without having to revise whole systems
- Make the server do the heavy lifting
  - Makes the specifications needed to run the application lower

## Website Application

The main reason why we went with a web application is based on the team's experience and skills on programming. The way we want this website to be setup would include the following pages.

### Front Page

This page would be the first page that would be shown when visiting our website

This website would include:

- Login - Logins for Drone Operators/Manager/Customers, once logged in they can access the appropriate pages.
- Sign up - Sign up new user / Sign up for drone operators
- Order - goes to the order page for customer or guest to order food
- Company goods - display company news for the customer
- Contact - leads to the contact page

### Sign Up / Login pages

These page would only be for login/signing up too accounts only

- Login - Logins for Drone Operators/Manager/Customers, once logged in they can access the appropriate pages.
- Sign up - Sign up new user / Sign up for drone operators

### Profile/Customer Page

This page would be the page the customer can access if they sign in to their profile

This page would include:

- Previous Orders - list of the customer previous orders
- Customer information - the customer address, name, etc..
- Contact - goes to the contact page

### Order Page

This page would be the page to order goods from the company

This page would include:

- Shop / cart - the shop that would include all the ice cream flavors and cones. Also the cart that the customer have to see what is ordered
- Request customer info - request customer information for delivery
- Order details - current order and order status

### Manager page

This page would be the page only for the manager to see

This page would include:

- Revenue - company current revenue
- Inventory - company current inventory
- Expense - company current "daily" expenses
- Customer - customers trying to contact the

### Drone operator page

This page would be for the only for the drone operator

- Drone inventory - the drone operator can access this page
- Add drones - the drone operator would be able to add new drones

### Contact Page

This page would be the only way to contact between us and the customers other than the order pages

- Customer info - would ask for customers information to contact customer

## UML Diagram

![./img/UML.jpg](./img/UML.jpg)
