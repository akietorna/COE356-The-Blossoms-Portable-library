from blossoms.settings import *
from blossoms.models.courses_model import *
from blossoms.models.books_model import *


# the class Movie will inherit the db.Model of SQLAlchemy
class Books_courses(db.Model):
    __tablename__ = 'books_courses'  # creating a table name
    id = db.Column(db.Integer, primary_key=True)  # this is the primary key
    book_link = db.Column(db.String(500), nullable=False)  # todo foreign key todo either book link or id
    # nullable is false so the column can't be empty
    course_code = db.Column(db.String(10), nullable=False)  # todo foreign key

    def json_books_courses(self):
        return {
                'link': self.book_link,
                'course_code':self.course_code,
            }



    def add_book_course(_link, _course_code):
        new_book_course = Books_courses(book_link= _link, course_code= _course_code)

        book_exists = Books.get_book(_link=_link)
        print(book_exists)
        course_exists = Courses.get_course(_code= _course_code)
        print(course_exists)

        if len(book_exists) > 0 and len(course_exists) > 0:
            relationship_already_added = Books_courses.get_books_for_course(_course_code=_course_code)

            if len(relationship_already_added) > 0:
                return 'relationship already added'
            db.session.add(new_book_course)
            db.session.commit()
            print('Book Course added')
            return ('Book Course added')
        else:
            return 'Either of courses or books doesnt exist, check it out'

    def get_all_books_courses(i=None):
        return [Books_courses.json_books_courses(book_course) for book_course in Books_courses.query.all()]

    def get_books_for_course(_course_code):
        result = Books_courses.query.filter_by(course_code = _course_code).all()
        print(result)
        if result==None:
            return []
        return [Books_courses.json_books_courses(item) for item in result]

    def get_book_course_rel(_course_code, _link):
        results = Books_courses.query.filter_by(course_code = _course_code, book_link=_link).first()
        print(results)
        if results==None:
            return []
        return [Books_courses.json_books_courses(results)]

    def update_book_course(_link, _course_code, _new_link):
        relationship_already_added = Books_courses.get_book_course_rel(_course_code=_course_code, _link=_link)
        if len(relationship_already_added) > 0:
            book_exists = Books.get_book(_link=_new_link)
            if len(book_exists) > 0:
                book_course_to_update = Books_courses.query.filter_by(book_link=_link, course_code=_course_code).first()
                book_course_to_update.book_link = _new_link
                db.session.commit()
                #print('updated')
                return('updated')
            else:
                return 'Book doesnt exist'
        else:
            return 'relationship doesnt exist'


    def delete_book_course(_link, _course_code):
        relationship_already_added = Books_courses.get_book_course_rel(_course_code=_course_code, _link=_link)
        if len(relationship_already_added) > 0:
            Books_courses.query.filter_by(book_link=_link, course_code = _course_code).delete()
            db.session.commit()
            print('deleted')
            return('deleted')
        else:
            print('relationship doesnt exist')
            return ('relationship doesnt exist')


if __name__ == '__main__':
    #print(Books_courses.add_book_course('1', 'Math 352'))
    #print(Books_courses.get_books_for_course('Math 351'))
    print(Books_courses.get_all_books_courses())
    #print(Books_courses.update_book_course(_link='2', _course_code='Math 352', _new_link='3'))
    #print(Books_courses.delete_book_course(_link='3', _course_code='Math 352'))