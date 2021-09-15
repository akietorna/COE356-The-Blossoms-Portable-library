from backend.blossoms1.settings import *
from backend.blossoms1.models.courses_model import *


# the class Movie will inherit the db.Model of SQLAlchemy
class Preps(db.Model):
    __tablename__ = 'preps'  # creating a table name
    id = db.Column(db.Integer, primary_key=True)  # this is the primary key
    name = db.Column(db.String(100), nullable=False)
    link = db.Column(db.String(500), nullable=False)
    # nullable is false so the column can't be empty
    course_code = db.Column(db.String(10), nullable=False)  # todo foreign key

    def json_preps(self):
        return {'id': self.id, 'name': self.name,
                'link': self.link, 'course_code': self.course_code}
        # this method we are defining will convert our output to json

    def add_prep(_name, _link, _course_code):
        new_prep = Preps(link=_link, course_code=_course_code, name=_name)

        course_exists = Courses.get_course(_code=_course_code)
        print(course_exists)

        if len(course_exists) > 0:
            prep_already_added = Preps.get_prep(_link=_link)

            if len(prep_already_added) > 0:
                return 'prep already exists'
            db.session.add(new_prep)
            db.session.commit()
            print('Prep added')
            return 'Prep added'
        else:
            return 'Course doesnt exist, check it out'

    def get_all_preps(i=None):
        return [Preps.json_preps(item) for item in Preps.query.all()]

    def get_preps_for_course(_course_code):
        result = Preps.query.filter_by(course_code=_course_code).all()
        print(result)
        if result == None:
            return []
        return [Preps.json_preps(slide) for slide in result]

    def get_prep(_link):
        results = Preps.query.filter_by(link=_link).first()
        print(results)
        if results == None:
            return []
        return [Preps.json_preps(results)]

    def update_prep(_link, _new_link, _code=None):
        prep_added = Preps.get_prep(_link=_link)
        if len(prep_added) > 0:
            prep_to_update = Preps.query.filter_by(link=_link).first()
            prep_to_update.link = _new_link
            if _code == None:
                pass
            else:
                prep_to_update.course_code = _code
            db.session.commit()
            print('updated')
            return 'updated'
        else:
            return 'Prep doesnt exist'

    def delete_prep(_link):
        prep_added = Preps.get_prep(_link=_link)
        if len(prep_added) > 0:
            Preps.query.filter_by(link=_link).delete()
            db.session.commit()
            print('deleted')
            return 'deleted'
        else:
            print('Prep doesnt exist')
            return 'Prep doesnt exist'


if __name__ == '__main__':
    # db.create_all()
    #print(Preps.add_prep(_name='ox', _link='5', _course_code='Math 351'))
    # print(Preps.get_prep(_link='1'))
    #print(Preps.get_preps_for_course(_course_code='Math 351'))
    print(Preps.get_all_preps())
    #print(Preps.update_prep(_link='2', _new_link='2'))
    # print(Preps.delete_prep(_link='2'))
