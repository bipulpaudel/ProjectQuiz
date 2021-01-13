from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from random import shuffle

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
db = SQLAlchemy(app)


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
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def shuffle(self):
        shuffle(self.questions)

    def display_name(self):
        print(self.name)
"""
class User:  # remove this relation
    def __init__(self, email, password, name, score, total_score):
        self.email = email
        self.password = password
        self.name = name
        self.score = score
        self.total_score = total_score

    def display_name(self):
        print(name)

    def increase_score():
        pass
"""
class Questions: 
    def __init__(self, id, question, category_id, option1, option2, option3, option4, correct_answer):
        self.id = id
        self.question = question
        self.category_id = category_id
        self.option1 = option1
        self.option2 = option2
        self.option3 = option3
        self.option4 = option4
        self.correct_answer = correct_answer

    def display_question(self):
        pass

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


 

#database for the categories
class Categories(db.Model):
    name = db.Column(db.String(30), nullable = False)
    id = db.Column(db.Integer, nullable = False, primary_key = True)
"""
#database for User
class userInfo(db.Model): # don't make login option for now
    name = db.Column(db.String(30), nullable = False)
    email = db.Column(db.String(20), nullable = False, primary_key = True)
    
    enc_password = db.Column(db.String(120), nullable = False) # create another column to keep track of the scores of the user 

    #hashing user's password
    def set_password(self, password):
        self.enc_password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.enc_password, password)

    """


#database for question and answer:
class Questions(db.Model): 
    id = db.Column(db.Integer, nullable = False, primary_key = True)
    question = db.Column(db.String(100), nullable = False)
    category_id = db.Column(db.Integer, nullable = False)
    option1 = db.Column(db.String(100), nullable = False)
    option2 = db.Column(db.String(100), nullable = False)
    option3 = db.Column(db.String(100), nullable = False)
    option4 = db.Column(db.String(100), nullable = False)
    correct_answer = db.Column(db.String(100), nullable = False)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/Categories', methods = ['GET', 'POST'])
def categories():
    if request.method == 'POST':
        category_name = request.form['name']
        new_category = Categories(name = category_name)
        db.session.add(new_category)
        db.session.commit()
        return redirect('/Categories')
    else:
        all_categories = Categories.query.all()
        return render_template('categories.html', categories = all_categories)


@app.route('/Questions', methods = ['GET', 'POST'])
def questions():
    if request.method == 'POST':
        question_question = request.form['question']
        question_category_id = request.form['category_id']
        question_option1 = request.form['option1']
        question_option2 = request.form['option2']
        question_option3 = request.form['option3']
        question_option4 = request.form['option4']
        question_correct_answer = request.form['correct_answer']
        new_question = Questions(question = question_question, category_id = question_category_id, option1 = question_option1, option2 = question_option2, option3 = question_option3, option4 = question_option4, correct_answer = question_correct_answer)
        db.session.add(new_question)
        db.session.commit()
        return redirect('/Questions')
    else:
        all_questions = Questions.query.all()
        return render_template('questions.html', questions = all_questions)


@app.route('/Categories/delete_category/<int:id>')
def delete_category(id):
    category = Categories.query.get_or_404(id)
    db.session.delete(category)
    db.session.commit()
    return redirect('/Categories')

@app.route('/Categories/edit_category/<int:id>', methods = ['GET', 'POST'])
def edit_category(id):
    category = Categories.query.get_or_404(id)
    if request.method == 'POST':
        category.name = request.form['name']
        db.session.commit()
        return redirect('/Categories')
    else:
        return render_template('edit_category.html', category = category)

@app.route('/Categories/new_category', methods = ['GET', 'POST'])
def new_category():
    if request.method == 'POST':
        category_name = request.form['name']
        new_category = Categories(name = category_name)
        db.session.add(new_category)
        db.session.commit()
        return redirect('/Categories')
    else:
        return render_template('new_category.html')


@app.route('/Questions/delete_question/<int:id>')
def delete_question(id):
    question = Questions.query.get_or_404(id)
    db.session.delete(question)
    db.session.commit()
    return redirect('/Questions')

@app.route('/Questions/edit_question/<int:id>', methods = ['GET', 'POST'])
def edit_question(id):
    question = Questions.query.get_or_404(id)
    if request.method == 'POST':
        question.question = request.form['question']
        question.category_id = request.form['category_id']
        question.option1 = request.form['option1']
        question.option2 = request.form['option2']
        question.option3 = request.form['option3']
        question.option4 = request.form['option4']
        question.correct_answer = request.form['correct_answer']
        db.session.commit()
        return redirect('/Questions')
    else:
        return render_template('edit_question.html', question = question)

@app.route('/Questions/new_question', methods = ['GET', 'POST'])
def new_question():
    if request.method == 'POST':
        question_question = request.form['question']
        question_category_id = request.form['category_id']
        question_option1 = request.form['option1']
        question_option2 = request.form['option2']
        question_option3 = request.form['option3']
        question_option4 = request.form['option4']
        question_correct_answer = request.form['correct_answer']
        new_question = Questions(question = question_question, category_id = question_category_id, option1 = question_option1, option2 = question_option2, option3 = question_option3, option4 = question_option4, correct_answer = question_correct_answer)
        db.session.add(new_question)
        db.session.commit()
        return redirect('/Questions')
    else:
        return render_template('new_question.html')



if __name__ == "__main__":
    app.run(debug = True)





















