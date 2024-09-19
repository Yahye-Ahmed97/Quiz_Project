import mysql.connector

# Establish connection to database
def connect_to_database():
    connection = mysql.connector.connect(
        host = "localhost",
        user = "Project_01",
        password = "2877@smn",
        database = "quiz_system"
    )

    return connection


# create a function to add questions to the database

def add_question():
    connection = connect_to_database()
    cursor = connection.cursor()

    # Get question details from the user

    question = input("Enter the question : ")
    option1 = input("Enter option 1 : ")
    option2 = input("Enter option 2 : ")
    option3 = input("Enter option 3 : ")
    option4 = input("Enter option 4 : ")
    correct_asnwer = int(input("Enter the correct option number {1-4} : "))

    # insert the question to the database

    query = "INSERT INTO questions (question_text, option1, option2, option3, option4, correct_answer) VALUES(%s, %s, %s, %s, %s, %s)"
    values = (question, option1, option2, option3, option4, correct_asnwer)
    cursor.execute(query, values)

    # commit the transaction

    connection.commit()

    print("question added successfully")
    cursor.close()
    connection.close()


# function to let the user to take the quiz

def take_quiz():

    connection = connect_to_database()
    cursor = connection.cursor()

    # get the user's name

    user_name = input("Enter your name : ")
    total_score = 0

    # fetch all questions from the database

    cursor.execute("SELECT * FROM questions")

    questions = cursor.fetchall()

    # loop through each user and ask the user
    for question in questions:
        print("\n" + question[1])
        print("1. " + question[2])
        print("2. " + question[3])
        print("3. " + question[4])
        print("4. " + question[5])

        # get the user's answer

        user_answer = int(input("your answer (1-4) : "))

        # check if the answer is correct

        if user_answer == question[6]:
            print("correct!")
            total_score += 1

        else:
            print("wrong answer! the correct answer is option", question[6])

    # insert user's score into the user's table

    cursor.execute("INSERT INTO users (name, score) VALUES (%s, %s)", (user_name, total_score))
    connection.commit()

    print(f"\n quiz finished! {user_name}, your score is : {total_score}/{len(questions)}")

    cursor.close()

    connection.commit()

# function to display the high scores

def display_high_scores():
    connection = connect_to_database()
    cursor = connection.cursor()

    # fetch top 5 scores

    cursor.execute("SELECT name, score FROM users ORDER BY score DESC LIMIT 5")

    high_scores = cursor.fetchall()

    print("\n----------High Scores : ----------------")
    for score in high_scores:
        print(f"{score[0]} : {score[1]} points")

    cursor.close()

    connection.close()


# main menu


def menu():
    while True:
        print("\nQuiz System")
        print("1. Add a question")
        print("2. Take the quiz")
        print("3. Display high scores")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            add_question()
        elif choice == '2':
            take_quiz()
        elif choice == '3':
            display_high_scores()
        elif choice == '4':
            print("Exiting the quiz system. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")



# run the menu

menu()

