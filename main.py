from flask import Flask, flash, redirect, render_template, request, session

from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['DEBUG'] = True
#code on line below used to connect this program to a database
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://build-a-blog:password@localhost:8889/build-a-blog'
app.config['SQLALCHEMY_ECHO'] = True # allows us to see the SQL in the terminal after the command has been completed
app.secret_key = 'ahduED43W' # secrect key used to denote a unque session


db = SQLAlchemy(app)


# model for the Task table in the database
class Blog(db.Model):

    id = db.Column(db.Integer, primary_key = True) # creates a primary key denoted sequently after each task object is created
    title = db.Column(db.String(120))
    blog_post = db.Column(db.String(420))
    # owner_id =db.Column(db.Integer, db.ForeignKey('user.id'))

    #creates a task object with name, owner data passed in the call of the task object
    def __init__(self, title, blog):
        self.title = title
        self.blog_post = blog
        # self.owner = owner
       




# class User(db.Model):

#     id= db.Column(db.Integer, primary_key=True)
#     email = db.Column(db.String(120), unique = True)
#     password = db.Column(db.String(120))
#     task = db.relationship('Task', backref='owner')

#     def __init__(self,email, password):
#         self.email = email
#         self.password = password


@app.route('/', methods=['POST', 'GET'])
def index():

    # owner = User.query.filter_by(email=session['email']).first()    

    if request.method == 'POST':

        title = request.form['title']
        blog_body = request.form['body']
        new_blog = Blog(title, blog_body)
        db.session.add(new_blog)
        db.session.commit()

        

        # removed list adder to accomdate database functionality
        # tasks.append(task_name)
    # tasks = Task.query.all() this query gets all items in the database
    # tasks = Task.query.filter_by(completed=False, owner=owner).all()
    # completed_tasks = Task.query.filter_by(completed=True, owner= owner).all()
    return render_template('blog.html',title="The Blog!")


# @app.route('/delete-task', methods=['POST'])
# def delete_task():

#     task_id = int(request.form['task-id'])
#     task = Task.query.get(task_id)
#     task.completed = True

#     # removes the deletion of the task form the database
#     # db.session.delete(task)
#     db.session.add(task)
#     db.session.commit()

#     return redirect('/')


# @app.before_request
# def require_login():

#     allowed_routes = ['login', 'register']

#     if request.endpoint not in allowed_routes and 'email' not in session:
#         return redirect('/login')

# @app.route('/login', methods=['POST','GET'])
# def login():

#     if request.method == 'POST':
#         email = request.form['email']
#         password = request.form['password']
#         user = User.query.filter_by(email = email).first()

#         if user and user.password == password:
#             #TODO remeber user has logined
#             session['email'] = email
#             flash("Logged In")
#             print(session)
#             return redirect('/')
#         else:
#             #TODO expalin why login failed
#             flash('User password incorrect, or User does not exist', 'error')
            


#     return render_template('login.html')


# @app.route('/register', methods=['POST','GET'])
# def register():

#     if request.method == 'POST':
#         email = request.form['email']
#         password = request.form['password']
#         verify = request.form['verify']

#         #TODO validate user's data

#         existing_user = User.query.filter_by(email = email).first()

#         if password != verify:
#             return "<h1> passwords dont match </h1>"

#         if not existing_user:
#             new_user = User(email, password)
#             db.session.add(new_user)
#             db.session.commit()
#             #TODO - remeber the user
#             session['email'] = email
#             return redirect('/')
#         else:
#             # TODO - Better User response
#             return "<h1>Duplicate User</h1>"

#     return render_template('register.html')


# @app.route('/logout')
# def logout():
#     del session['email']
#     return redirect('/')


if __name__ == '__main__':
    app.run()
