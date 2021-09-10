from settings import *


# the class Movie will inherit the db.Model of SQLAlchemy
class Videos_courses(db.Model):
    __tablename__ = 'videos_courses'  # creating a table name
    id = db.Column(db.Integer, primary_key=True)  # this is the primary key
    link = db.Column(db.String(500), nullable=False)  # todo foreign key
    # nullable is false so the column can't be empty
    course_code = db.Column(db.String(10), nullable=False)  # todo foreign key

    def create_independent_tables(self):
        # todo programs, books, courses, videos, projects
        self.create_programs_table()
        self.create_books_table()
        self.create_courses_table()
        self.create_videos_table()
        self.create_projects_table()

    def create_dependent_tables(self):
        # todo programs_courses, preps, slides, videos_courses, books_courses
        self.create_programs_courses_table()
        self.create_preps_table()
        self.create_slides_table()
        self.create_videos_courses_table()
        self.create_books_courses_table()

    def json(self):
        return {'id': self.id, 'title': self.title,
                'year': self.year, 'genre': self.genre}
        # this method we are defining will convert our output to json

    def add_movie(_title, _year, _genre):
        '''function to add movie to database using _title, _year, _genre
        as parameters'''
        # creating an instance of our Movie constructor
        new_movie = Movie(title=_title, year=_year, genre=_genre)
        db.session.add(new_movie)  # add new movie to database session
        db.session.commit()  # commit changes to session

    def add_program(self, name, about, department):
        pass

    def get_all_movies(i=None):
        '''function to get all movies in our database'''
        return [Movie.json(movie) for movie in Movie.query.all()]

    def get_movie(_id):
        '''function to get movie using the id of the movie as parameter'''
        return [Movie.json(Movie.query.filter_by(id=_id).first())]
        # Movie.json() coverts our output to the json format defined earlier
        # the filter_by method filters the query by the id
        # since our id is unique we will only get one result
        # the .first() method will get that first value returned

    def update_movie(_id, _title, _year, _genre):
        '''function to update the details of a movie using the id, title,
        year and genre as parameters'''
        movie_to_update = Movie.query.filter_by(id=_id).first()
        movie_to_update.title = _title
        movie_to_update.year = _year
        movie_to_update.genre = _genre
        db.session.commit()

    def delete_movie(_id):
        '''function to delete a movie from our database using
           the id of the movie as a parameter'''
        Movie.query.filter_by(id=_id).delete()
        # filter movie by id and delete
        db.session.commit()  # commiting the new change to our database


if __name__ == '__main__':
    db.create_all()
