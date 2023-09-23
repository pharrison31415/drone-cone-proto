# High Level Design Document

## Frameworks and Programming Languages
### Django - Backend Development

The system logic and backend development will be implemented on the Django Framework. Django is a python based web development framework designed to help web developers develop their applications as smoothly as possible by providing the base requirements need for a web app. This framework provides simpler implementation of views, templates, and databases. Django provides compatibility with several different types of databases. This allows web developers to be able to choose based on their own abilities and what individual projects require. Django also provides API abilities which allows for easier integration with other frameworks and programs.

The design of the Django framework is ideal for the Drone Cones backend system for the following reasons:
* Choose a database (MySQL) that is easy to work with and effectively stores necessary data
* Use a high level language that provides smooth transitioning from design to implementation
* Use relevant and well known framework and language that will be easier to train new people on as the application grows
* Use API capabilities to connect with front end framework for smooth communication of information between the server and the user

### Svelte - Frontend Development

The frontend and the visuals will be implemented on a Svelte framework. Svelte is a reactive UI framework. Svelte is a javascript based web development framework designed to help with HTML, CSS, JavaScript, and UI that would react to changes in the data. This framework provides no virtual DOM, providing reconcile changes and update the actual DOM. It updates the elements directly as the data changes, which results in faster updates and less memory overhead. Svelte also provides scopred styling to help prevent unintentional style conflicts. Svelte also provides HTML, CSS and JavaScript integrations, letting you write component templates in HTML, styles in CSS, and logic in JavaScript. Svelte also has animation support to easily create smooth transitions and animations within. Svelte makes it straightforward to handle form inputs, events, and user interactions, simpliflying common tasks like form validation and event handling.

The design of the Svelte framework is ideal for the Drone Cones frontend system for the following reasons:
* A highly optimized JavaScript during build time.
* Small bundle sizes, Svelte generates smaller JavaScript bundles.
* Simplicity, Svelte's syntax and approach is relatively simple and easy to learn.
* Reactivity to data changes to the backend.
* No runtime framework overhead, code is as close to native JavaScript as possible.
* Small bundle sizes make it well-suited for building mobile-responsive websites that perform well on a variety if devices.


### Architecture

The system will architechture will be a 2-tier Client/Server Architecture. This means that the information the application will need will be accessed through protocol. 

Using a 2-tier client/server architecture is ideal for Drone Cones for the following reasons:
* Establish a secure way to transfer data between client and server
* Protocol tightly joins client with server, so when server is being updated, client is being changed to match
* The application can be run on multiple computers without having to scale the servers as much
  * Amount of clients per server is not 1:1
* Implementation of a 2-tier Client/Server Architecture will allow us to properly scale once we are done prototyping without having to revise whole systems
* Make the server do the heavy lifting
  * Makes the specifications needed to run the application lower


