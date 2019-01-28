from flask import Flask, render_template

# name of the module = __name__
# where the flask looks for the flask files
app = Flask(__name__)

posts = [
        {
            'author': 'arvin',
            'title': 'Blog Post 1',
            'content': 'first post content',
            'date_posted': 'April 20, 2018'
            },
{
            'author': 'arvin',
            'title': 'Blog Post 2',
            'content': 'second post content',
            'date_posted': 'April 20, 2018'
            }
        ]

# this is the url
# urls are the app.route
@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)

@app.route("/about")
def about():
    return render_template('about.html')













# create a python file with the from flask import FLASK
# in the terminal export FLASK_APP=your flask title
# do flask run
# to turn on debug mode - export FLASK_DEBUG=1

if __name__ == '__main__':
    app.run(debug=True)


