from flask import Flask, render_template
app = Flask(__name__, template_folder='backend/templates')

posts = [
    {
        'author': 'Tony Blaise',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'March 19, 2024'
    },
    {
        'author': 'John arm',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'March 20, 2024'
    },
    {
        'author': 'Jonny wilder',
        'title': 'Blog Post 3',
        'content': 'Second post content',
        'date_posted': 'March 22, 2024'
    },
    {
        'author': 'Harry Jim',
        'title': 'Blog Post 3',
        'content': 'Third post content',
        'date_posted': 'March 24, 2024'
    },
    {
        'author': 'Pavel',
        'title': 'Blog Post 4',
        'content': 'Fourth post content',
        'date_posted': 'March 25, 2024'
    },
    {
        'author': 'Fiacre',
        'title': 'Blog Post 5',
        'content': 'Firth post content',
        'date_posted': 'March 27, 2024'
    }
]
@app.route("/")
@app.route("/home")
def hello():
    return render_template('home.html', posts=posts)


@app.route("/about")
def about():
    return  render_template('about.html')


if __name__ == '__main__':
    app.run(debug=True)
