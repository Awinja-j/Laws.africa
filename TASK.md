# Law.Africa

# Python Developer Challenge: a basic leave request submission system

Create a simple leave submission system that allows a user to list, submit and edit leave requests for company staff.

Note: I am most interested in how you approach the problem, how you design your solution, and your motivation for the choices you make.

### Functional requirements

The user must be able to:

* List submitted leave requests, including the number of leave days requested for each leave request
* Submit a new leave request
* Edit an existing leave request

A leave request has the following properties (you must choose appropriate Django model fields for these properties):

* The person the leave request is being submitted for
* The starting and ending dates of the period of leave
* Whether the request is for normal leave or sick leave

### Technical requirements

* Use a currently supported version of Python 3
* Use Django 3.2
* Use a SQLight database file

### Bonus functionality

Optional additional functionality:

* When calculating the number of leave days for a request, do not count weekends (ie. only count week days) 

## Not required

* There is no need to have user authentication. Anyone can use the system.
* There is no need to apply CSS or styling to your application. Basic HTML is sufficient.

## Submitting your challenge solution

You can submit your challenge solution as:

* a github repo
* a zip file

When submitting, include:

* a basic README explaining how to install and run your application
* a requirements.txt file with any necessary depedencies
* any required Django migrations

Submit your challenge to greg@laws.africa.

## Duration

This challenge should take one to two hours to complete.