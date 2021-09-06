from blossoms.settings import *


# the class Movie will inherit the db.Model of SQLAlchemy
class Books_courses(db.Model):
    __tablename__ = 'books_courses'  # creating a table name
    id = db.Column(db.Integer, primary_key=True)  # this is the primary key
    book_link = db.Column(db.String(500), nullable=False)  # todo foreign key todo either book link or id
    # nullable is false so the column can't be empty
    course_code = db.Column(db.String(10), nullable=False)  # todo foreign key

    def json_books_courses(self):
        return {
                'link': self.link,
                'course_code':self.course_code,
            }



    def add_book_course(_link, _course_code):
        new_book_course = Books_courses(link= _link, course_code= _course_code)
        db.session.add(new_book_course)
        db.session.commit()

    def get_all_books_courses(i=None):
        return [Books_courses.json_books_courses(book_course) for book_course in Books_courses.query.all()]

    def get_books_for_course(_course_code):
        result = Books_courses.query.filter_by(course_code = _course_code).all()
        print(result)
        if result==None:
            return []
        return [Books_courses.json_books_courses(item) for item in result]

    def update_book_course(_link, _course_code, _new_link):
        book_course_to_update = Books_courses.query.filter_by(link=_link, course_code= _course_code).first()
        book_course_to_update.link = _new_link
        db.session.commit()


    def delete_book_course(_link, _course_code):
        Books_courses.query.filter_by(link=_link, course_code = _course_code    ).delete()
        db.session.commit()


if __name__ == '__main__':
    db.create_all()