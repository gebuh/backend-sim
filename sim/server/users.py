from sim.server.db import db


class Users(db.Model):
    __tablename__ = "users"
    user_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80))
    password = db.Column(db.String())
    role_id = db.Column(db.Integer)
    status = db.Column(db.Integer)
    created_date = db.Column(db.String())
    updated_date = db.Column(db.String())

    def __init__(self, username, password):
        self.username = username
        self.password = password


    def json(self):
        return {
                   "id": self.user_id,
                   "username": self.username
               }, 200

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def remove_from_db(self):
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def find_user_by_username(cls, username):
        return cls.query.filter_by(username=username).first()

    @classmethod
    def find_user_by_id(cls, _id):
        return cls.query.filter_by(user_id=_id).first()
