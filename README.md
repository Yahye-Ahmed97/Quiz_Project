A simple quiz application built with Python and MySQL. 

This app allows users to add questions, take quizzes, and view high scores.

Features


Add questions to the database
Take a quiz and receive scores
Display top scores


Requirements

Python 3.x
MySQL Connector (mysql-connector-python)


Setup


Create a MySQL database named quiz_system.

Create two tables:

questions: to store quiz questions.
users: to store user names and scores.
Update the database connection parameters in connect_to_database() function.

Usage

Run the application and select options from the menu:

Add a question
Take the quiz
Display high scores
Exit
