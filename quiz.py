from flask import Flask
from flask_sqlalchemy import SQLAlchemy



# first option in the list are always the correct answer
"""
practice_questions = {'Python':
            [("How do you insert COMMENTS in Python code?",["#comment", "//comment", "/*comment*/"]),
            ("Which one is NOT a legal variable name?",["my-Var", "myVar", "myVar"])],

            'C++':
            [("How do you create a variable with the numeric value 5?", ["int x = 5", "double x = 5", "x = 5"]),
            ("Which method can be used to find the length of a string?", ["length()", "getSize()", "len()"])]
            }
"""
# class categories to distinguish the categories of questions
class Categories:
    def __init__(self, name, questions, id):
        self.name = name
        self.practice_questions = questions
        self.id = id

    def shuffle(self):
        pass


    

class User:
    def __init__(self, email, password, name):
        self.email = email
        self.password = password
        self.name = name

    def display_name(self):
        print(name)

class Question:
    def __init__(self, question, category_id):
        self.question = question
        self.category_id = category_id

    def display_question(self):
        pass

class Options:
    def __init__(self, options, correct):
        self.options = options
        self.correct_option = options[correct]

    def display_options(self):
        pass

# checks whether the user answer is correct or incorrect
def answer_check(user_answer):
    pass

# updates the score of the user after each question
def update_score(current_score):
    pass

def display_result(correct, incorrect, score):
    pass


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
db = SQLAlchemy(app) 

#database for User
class userInfo(db.Model):
    name = db.Column(db.String(30), nullable = False)
    email = db.Column(db.String(20), nullable = False, primary_key = True)
    enc_password = db.Column(db.String(120), nullable = False)

    #hashing user's password
    def set_password(self, password):
        self.enc_password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.enc_password, password)

    


#database for question and answer:
class quiz(db.Model):
    question = db.Column(db.String(100), nullable = False)
    options = db.Column(db.String(100), nullable = False) # convert options list to a string and store it here later convert that string to a list






