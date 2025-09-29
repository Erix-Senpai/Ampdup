class Event:

    def __init__(self, name, description, image, currency):
        self.name = name
        self.description = description
        self.image = image
        self.currency = currency
        self.comments = list()

    def set_comments(self, comment):
        self.comments.append(comment)

    def __repr__(self):
        str = f"Name: {self.name}, Currency: {self.currency}"
        return str

class Comment:
    def __init__(self,user, text, created_at):
        self.user = user
        self.text = text
        self.created_at = created_at

    def __repr__(self):
        str = f"User {self.user}, \n Text {self.text}"
        return str
    

from Ampdup_Codebase import db
class User(db.Model):
    id          = db.Column(db.Integer,     primary_key = True)
    user_name   = db.Column(db.String(20),  unique=False, nullable=False)
    email       = db.Column(db.String(40),  unique=False, nullable=False)
    password    = db.Column(db.String(20),  unique=False, nullable=False)

    def __repr__(self):
        str = f"User {self.user_name}, \n Text {self.password}"
        return str