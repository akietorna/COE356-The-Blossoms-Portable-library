from settings import *


# the class Movie will inherit the db.Model of SQLAlchemy
class Programs_courses(db.Model):
    __tablename__ = 'programs_courses'  # creating a table name
    id = db.Column(db.Integer, primary_key=True)  # this is the primary key
    program_name = db.Column(db.String(80), nullable=False)  # todo foreign key
    sem = db.Column(db.Integer, nullable=False)
    # nullable is false so the column can't be empty
    course_code = db.Column(db.String(10), nullable=False)  # todo foreign key

    def json_books(self):
        return {
            'name': self.name,
            'link': self.link,
            'isbn': self.isbn,
            'author': self.author,
            'publisher': self.publisher
        }

    def add_book(_name, _link, _isbn=' ', _author=' ', _publisher=' '):
        new_course = Books(name=_name, link=_link, isbn=_isbn,
                           author=_author, publisher=_publisher)
        db.session.add(new_course)
        db.session.commit()

    def get_all_books(i=None):
        return [Books.json_books(book) for book in Books.query.all()]

    def get_book(_link):
        result = Books.query.filter_by(link=_link).first()
        print(result)
        if result == None:
            return []
        return [Books.json_books(result)]

    def update_book(_link, _name):
        book_to_update = Books.query.filter_by(link=_link).first()
        book_to_update.name = _name
        book_to_update.link = _link
        db.session.commit()

    def delete_book(_link):
        Books.query.filter_by(link=_link).delete()
        db.session.commit()


if __name__ == '__main__':
    db.create_all()
