from flask import Flask, request, redirect, render_template
import jinja2
import os

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir), autoescape=True)

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/')
def index():

    return render_template('user_signup.html', username='', username_error='', password='', password_error='', verifypwd='', verifypwd_error='', email='',email_error='', title="Sign Up", stylesheet="static/styles.css")

def is_name_valid(name):
    try:
        if len(name) in range (3,21) and ' ' not in name:
            return True
    except ValueError:
        return False

def is_pw_valid(pw):
    try:
        if len(pw) in range (3,21) and ' ' not in pw:
            return True
    except ValueError:
        return False

def is_email(email):
    try:
        if email == '':
            return True
        elif len(email) in range (3,21) and ' ' not in email and'@' in email and '.' in email:
            return True
    except ValueError:
        return False
          
@app.route('/', methods = ['POST'])
def validate_form():

    username = request.form['username']
    password = request.form['password']
    verifypwd = request.form['verifypwd']
    email = request.form['email']

    username_error = ''
    password_error = ''
    verifypwd_error = ''
    email_error = ''

    if not is_name_valid(username):
        username_error = "Not a valid username. See requirements below."
        username = ''

    if not is_pw_valid(password):
        password_error = "Not a valid password. See requirements below."
        password = ''
        verifypwd = ''

    if password != verifypwd:
        verifypwd_error = "Your passwords do not match.  Please retype them and try again."
        verifypwd = ''
        password = ''
 
    if not is_email(email):
        email_error = "Not a valid email.  Please try again."
        email = ''
        password = ''
        verifypwd = ''

    if username_error == "Not a valid username. See requirements below.":
        password = ''
        verifypwd = ''
    
    if not username_error and not password_error and not verifypwd_error and not email_error:
        return render_template('welcome.html', username=username, title="Welcome!", stylesheet="static/styles.css")
    else:
        return render_template('user_signup.html', username_error=username_error, password_error=password_error, verifypwd_error=verifypwd_error, email_error=email_error, username=username, password=password, verifypwd=verifypwd, email=email,title="Sign Up", stylesheet="static/styles.css")


app.run()