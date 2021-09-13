from settings import *

# the class Movie will inherit the db.Model of SQLAlchemy


class Users(db.Model):
    __tablename__ = "Users"  # creating a table name
    user_id = db.Column(db.Integer, primary_key=True,
                        nullable=False)  # this is the primary key
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    user_name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(80), nullable=False)
    # nullable is false so the column can't be empty
    password = db.Column(db.String(150), nullable=True)

    def json_users(self):
        return {
            'first_name': self.first_name,
            'last_name': self.last_name,
            'user_name': self.user_name,
            'email': self.email,
            'password': self.password
        }

    def add_user(_first_name, _last_name, _user_name, _email, _password):
        new_user = Users(first_name=_first_name, last_name=_last_name,
                         user_name=_user_name, email=_email, password=_password)
        db.session.add(new_user)
        db.session.commit()

    def get_all_users():
        print('it is okay')
        users_list = json_user(Users.query.all())
        return users_list

    def get_user(_user_name):
        result = Users.query.filter_by(user_name=_user_name).first()
        if result == None:
            return []
        return [Users.json_users(result)]

    def update_user(_first_name, _last_name, _user_name, _email, _password):
        user_to_update = Users.query.filter_by(user_name=_user_name).first()
        user_to_update.first_name = _first_name
        user_to_update.last_name = _last_name
        user_to_update.user_name = _user_name
        user_to_update.email = _email
        user_to_update.password = _password
        db.session.commit()

    def reset_password(_user_name, _password):
        user_name = Users.query.filter_by(user_name=_user_name).first()
        user_name.password = _password
        db.session.commit()

    def delete_user(_user_name):
        Users.query.filter_by(user_name=_user_name).delete()
        db.session.commit()


if __name__ == '__main__':
    db.create_all()
