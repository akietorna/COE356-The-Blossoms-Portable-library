from backend.blossoms1.settings import *
from backend.blossoms1.models.courses_model import *


# the class Movie will inherit the db.Model of SQLAlchemy
class Slides(db.Model):
    __tablename__ = 'slides'  # creating a table name
    id = db.Column(db.Integer, primary_key=True)  # this is the primary key
    name = db.Column(db.String(100), nullable=False)
    link = db.Column(db.String(500), nullable=False)
    # nullable is false so the column can't be empty
    course_code = db.Column(db.String(10), nullable=False)  # todo foreign key

    def json_slides(self):
        return {'id': self.id, 'name': self.name,
                'link': self.link, 'course_code': self.course_code}
        # this method we are defining will convert our output to json

    def add_slide(_name, _link, _course_code):
        new_slide = Slides(link=_link, course_code=_course_code, name=_name)

        course_exists = Courses.get_course(_code=_course_code)
        print(course_exists)

        if len(course_exists) > 0:
            slide_already_added = Slides.get_slide(_link=_link)

            if len(slide_already_added) > 0:
                return 'Slide already added'
            db.session.add(new_slide)
            db.session.commit()
            print('Slide added')
            return 'Slide added'
        else:
            return 'Course doesnt exist, check it out'

    def get_all_slides(i=None):
        return [Slides.json_slides(slide) for slide in Slides.query.all()]

    def get_slides_for_course(_course_code):
        result = Slides.query.filter_by(course_code=_course_code).all()
        print(result)
        if result == None:
            return []
        return [Slides.json_slides(slide) for slide in result]

    def get_slide(_link):
        results = Slides.query.filter_by(link=_link).first()
        print(results)
        if results == None:
            return []
        return [Slides.json_slides(results)]

    def update_slide(_link, _new_link, _code=None):
        slide_added = Slides.get_slide(_link=_link)
        if len(slide_added) > 0:
            slide_to_update = Slides.query.filter_by(link=_link).first()
            slide_to_update.link = _new_link
            if _code == None:
                pass
            else:
                slide_to_update.course_code = _code
            db.session.commit()
            print('updated')
            return 'updated'
        else:
            return 'Slide doesnt exist'

    def delete_slide(_link):
        slide_added = Slides.get_slide(_link=_link)
        if len(slide_added) > 0:
            Slides.query.filter_by(link=_link).delete()
            db.session.commit()
            print('deleted')
        else:
            print('Slide doesnt exist')


if __name__ == '__main__':
    # db.create_all()
    #print(Slides.add_slide(_name='herh name', _link='4', _course_code='41'))
    print(Slides.get_slide(_link='1'))
    print(Slides.get_slides_for_course(_course_code='Math 351'))
    print(Slides.get_all_slides())
    #print(Slides.update_slide(_link='1', _new_link='2'))
    #print(Books_courses.update_book_course(_link='2', _course_code='Math 352', _new_link='3'))
    # print(Slides.delete_slide(_link='2'))
