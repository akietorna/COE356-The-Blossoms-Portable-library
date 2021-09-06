from blossoms.settings import *


# the class Movie will inherit the db.Model of SQLAlchemy
class Courses(db.Model):
    __tablename__ = 'courses'  # creating a table name
    id = db.Column(db.Integer, primary_key=True)  # this is the primary key
    name = db.Column(db.String(100), nullable=False)
    course_code = db.Column(db.String(10), nullable=False)
    # nullable is false so the column can't be empty
    about = db.Column(db.String(1000), nullable=True)


    # def json(self):
    #     return {'id': self.id, 'title': self.title,
    #             'year': self.year, 'genre': self.genre}
    #     # this method we are defining will convert our output to json

    def json_courses(self):
        return {
                'name': self.name,
                'course_code': self.course_code,
                'about': self.about
            }



    def add_course(_name,_code, _about):
        new_course = Courses(name = _name, course_code= _code, about=_about)
        db.session.add(new_course)
        db.session.commit()

    def get_all_courses(i=None):
        return [Courses.json_courses(course) for course in Courses.query.all()]

    # def get_movie(_id):
    #     '''function to get movie using the id of the movie as parameter'''
    #     return [Movie.json(Movie.query.filter_by(id=_id).first())]
    #     # Movie.json() coverts our output to the json format defined earlier
    #     # the filter_by method filters the query by the id
    #     # since our id is unique we will only get one result
    #     # the .first() method will get that first value returned

    def get_course(_code):
        result = Courses.query.filter_by(course_code = _code).first()
        print(result)
        if result==None:
            return []
        return [Courses.json_courses(result)]

    # def update_movie(_id, _title, _year, _genre):
    #     '''function to update the details of a movie using the id, title,
    #     year and genre as parameters'''
    #     movie_to_update = Movie.query.filter_by(id=_id).first()
    #     movie_to_update.title = _title
    #     movie_to_update.year = _year
    #     movie_to_update.genre = _genre
    #     db.session.commit()

    def update_course(_code, _name, _about):
        course_to_update = Courses.query.filter_by(course_code=_code).first()
        course_to_update.name = _name
        course_to_update.about = _about
        db.session.commit()

    # def delete_movie(_id):
    #     '''function to delete a movie from our database using
    #        the id of the movie as a parameter'''
    #     Movie.query.filter_by(id=_id).delete()
    #     # filter movie by id and delete
    #     db.session.commit()  # commiting the new change to our database


    def delete_course(_code):
        Courses.query.filter_by(course_code=_code).delete()
        db.session.commit()




# if __name__ == '__main__':
#     db.create_all()