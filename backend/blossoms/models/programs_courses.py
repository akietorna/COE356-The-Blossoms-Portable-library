from blossoms.settings import *
from blossoms.models.courses_model import *
from blossoms.models.programs_model import *


# the class Movie will inherit the db.Model of SQLAlchemy
class Programs_courses(db.Model):
    __tablename__ = 'programs_courses'  # creating a table name
    id = db.Column(db.Integer, primary_key=True)  # this is the primary key
    program_name = db.Column(db.String(80), nullable=False)  # todo foreign key
    sem = db.Column(db.Integer, nullable=False)
    # nullable is false so the column can't be empty
    course_code = db.Column(db.String(10), nullable=False)  # todo foreign key

    def json_programs_courses(self):
        return {'id': self.id,
                'program': self.program_name,
                'course_code': self.course_code,
                'sem':self.sem}
        # this method we are defining will convert our output to json

    def add_program_course(_prog, _course_code, _sem):
        new_prog_course = Programs_courses(course_code= _course_code, program_name=_prog, sem=_sem)

        course_exists = Courses.get_course(_code= _course_code)
        program_exists = Programs.get_program(_name=_prog)
        print(course_exists, program_exists)

        if len(course_exists) > 0 and len(program_exists)>0:
            prog_course_already_added = Programs_courses.get_prog_course_rel(_course_code=_course_code, _prog=_prog, _sem=_sem)

            if len(prog_course_already_added) > 0:
                return 'Program Course relationship already exists'
            db.session.add(new_prog_course)
            db.session.commit()
            print('Program Course relation added')
        else:
            return 'Either of Program or Course doesnt exist, check it out'

    def get_all_prog_courses(i=None):
        return [Programs_courses.json_programs_courses(item) for item in Programs_courses.query.all()]

    def get_courses_for_prog_for_sem(_prog, _sem):
        result = Programs_courses.query.filter_by(sem = _sem, program_name=_prog).all()
        print(result)
        if result==None:
            return []
        return [Programs_courses.json_programs_courses(item) for item in result]

    def get_prog_course_rel(_course_code, _prog, _sem):
        result = Programs_courses.query.filter_by(course_code = _course_code, program_name = _prog, sem=_sem).first()
        print(result)
        if result==None:
            return []
        return [Programs_courses.json_programs_courses(result)]


    def update_prog_course(_code,_sem, _prog, _new_code=None, _new_prog=None, _new_sem=None):
        prog_course_added = Programs_courses.get_prog_course_rel(_course_code=_code, _prog=_prog, _sem=_sem)
        if len(prog_course_added) > 0:
            prog_course_to_update = Programs_courses.query.filter_by(course_code=_code, program_name=_prog, sem=_sem).first()
            if _new_prog!=None:
                prog_course_to_update.program_name = _new_prog
            if _new_code!=None:
                prog_course_to_update.course_code = _new_code
            if _new_sem!=None:
                prog_course_to_update.sem = _new_sem
            db.session.commit()
            print('updated')
        else:
            return 'Program course relation doesnt exist'


    def delete_prog_course(_course,_sem, _prog):
        prog_cousrse_added = Programs_courses.get_prog_course_rel(_course_code=_course, _prog=_prog, _sem=_sem)
        if len(prog_cousrse_added) > 0:
            Programs_courses.query.filter_by(course_code=_course, program_name=_prog, sem=_sem).delete()
            db.session.commit()
            print('deleted')
        else:
            print('Program Course relation doesnt exist')



if __name__ == '__main__':
    #db.create_all()
    print(Programs_courses.delete_prog_course(_course='Math 351', _prog='computer', _sem=5))
    #print(Programs_courses.update_prog_course(_prog='computer', _sem=2, _code='Math 351'))
    #print(Programs_courses.get_prog_course_rel(_course_code='Math 351', _prog='computer', _sem=5))
    #print(Programs_courses.get_all_prog_courses())
    #print(Programs_courses.get_courses_for_prog_for_sem(_prog='computer', _sem=5))
    #print(Programs_courses.add_program_course(_prog='biomedical', _course_code='41', _sem=5))