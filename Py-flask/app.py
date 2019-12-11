from flask import Flask ,render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
db = SQLAlchemy(app)

class BlogPost(db.Model):
    id = db.Column(db.Integer , primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    author = db.Column(db.String(20), nullable=False,default='N/A')
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self):
        return 'Blog post ' + str(self.id)

all_posts = [
    {
        'title' : 'POst 1',
        'content':'THis is not bad',
        'author':'Kishore1'
    },
    {
        'title' : 'POst 2',
        'content':'THis is not bad 2',
        'author':'Kishore2'
    },
    {
        'title' : 'POst 3',
        'content':'THis is not bad 3',
        
    }
]


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/posts')
def posts():
    return render_template('posts.html',posts=all_posts)


@app.route('/<int:id>/<string:name>')
def hello(id,name):
    return "hello ,"+ name +" your id is "+str(id)
@app.route('/home/<string:name>')
def get_name(name):
    return "hello ,"+ name 
@app.route('/get', methods=['GET'])
def get():
    return "Only get req accepted "



if __name__=="__main__":
    app.run(debug=True)
