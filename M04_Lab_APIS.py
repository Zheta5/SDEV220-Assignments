from flask import Flask

app = Flask(__name__)
from flask_sqlalchemy import SQLAlchemy

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///books.db'
db = SQLAlchemy(app)
app.app_context().push()

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    book_name = db.Column(db.String(200), nullable=False)
    author_name = db.Column(db.String(200), nullable=False)
    year = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"Book('{self.book_name}', '{self.author_name}', '{self.year}')"
    

@app.route('/')
def index():
    return 'Hello World'

if __name__ == '__main__':
    app.run()