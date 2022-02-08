# Project 1

ENGO 551 - Alexandra Urbieta Torres

# The objectives of this lab were:
1. Become more comfortable with Python
2. Gain Experience with flask
3. Learn to use SQL to interact with databases

## STEP 1
Created a SQL database with 3 tables: users, books, and reviews. located in "database.sql"
Created an account in heroku to have access to a free PostgreSQL databse and obtain the URL to our app.


## STEP 2
Intead of "application.py" the main code to run the webpage is located in "main.py"
Inside the template folder there is access to the html files created
models.py contains the models for the registrarion of users and their location in a local database
database.db was created to save the user's information
views.py contain the home view for the website
auth.py contain the commands for the registration, login and logout authentication
import.py contains the function to read the books CSV file
__init__.py comtains the app information

## STEP 3
this step contains the information regarind the google books API and its implementation in the webpage. and also the code to search the books from our sql database.



### Built With
* [Flask](https://flask.palletsprojects.com/en/1.1.x/)
* [PostgreeSQL](https://www.postgresql.org/)
* [Bootstrap](https://getbootstrap.com)


### References
* ENGO551 - Lab 1 Assignment 
* Python Website Tutorial https://www.youtube.com/watch?v=dam0GPOAvVI&t=596s
* https://github.com/asperduti/cs50w
