#First code snippet
"""from flask import Flask
app = Flask(__name__)

if __name__ == '__main__':
   app.run(debug=True)"""

#Second code snippet
"""from flask import Flask, render_template, url_for
app = Flask(__name__)

posts = [
    {
        'author': 'Bob Dylan',
        'title': 'Why are there needs for titles?',
        'content': 'Content',
        'date_posted': 'May 17, 2020'
    },
    {
        'author': 'Joe Schmoe',
        'title': 'Welcome',
        'content': 'Content',
        'date_posted': 'October 16, 2020'
    }
]


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)


@app.route("/about")
def about():
    return render_template('about.html', title='About')


if __name__ == '__main__':
    app.run(debug=True)"""

#Third code snippet
"""from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = '41949efa0fce77d3d767ee372e32b09b'

posts = [
    {
        'author': 'Bob Dylan',
        'title': 'Why are there needs for titles?',
        'content': 'Content',
        'date_posted': 'May 17, 2020'
    },
    {
        'author': 'Joe Schmoe',
        'title': 'Welcome',
        'content': 'Content',
        'date_posted': 'October 16, 2020'
    }
]


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)


@app.route("/about")
def about():
    return render_template('about.html', title='About')


@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'test@gmail.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)


if __name__ == '__main__':
    app.run(debug=True)"""