from blossoms.models.courses_model import *


# the class Movie will inherit the db.Model of SQLAlchemy
class Projects(db.Model):
    __tablename__ = 'projects'  # creating a table name
    id = db.Column(db.Integer, primary_key=True)  # this is the primary key
    name = db.Column(db.String(100), nullable=False)
    link = db.Column(db.String(500), nullable=False)
    course = db.Column(db.String(10), nullable=False)


    def json_projects(self):
        return {'id': self.id,
                'name': self.name,
                'course_code': self.course,
                'link':self.link}
        # this method we are defining will convert our output to json

    def add_projects(_name, _course_code, _link):
        new_project = Projects(course= _course_code, name=_name, link=_link)

        course_exists = Courses.get_course(_code= _course_code)
        print(course_exists)

        if len(course_exists)>0:
            project_already_added = Projects.get_project(_link = _link)

            if len(project_already_added) > 0:
                return 'Project already exists'
            db.session.add(new_project)
            db.session.commit()
            print('Project added')
            return 'Project added'
        else:
            return 'Course doesnt exist, check it out'

    def get_all_projects(i=None):
        return [Projects.json_projects(item) for item in Projects.query.all()]

    def get_project(_link):
        result = Projects.query.filter_by(link = _link).first()
        print(result)
        if result==None:
            return []
        return [Projects.json_projects(result)]

    def get_projects_for_course(_course_code):
        result = Projects.query.filter_by(course = _course_code).all()
        print(result)
        if result==None:
            return []
        return [Projects.json_projects(item) for item in result]


    def update_project(_link, _new_code=None, _new_link=None, _new_name=None):
        project_added = Projects.get_project(_link=_link)
        if len(project_added) > 0:
            project_to_update = Projects.query.filter_by(link=_link).first()
            if _new_name!=None:
                project_to_update.name = _new_name
            if _new_code!=None:
                project_to_update.course = _new_code
            if _new_link!=None:
                project_to_update.link = _new_link
            db.session.commit()
            print('updated')
            return 'updated'
        else:
            return 'Project doesnt exist'


    def delete_project(_link):
        project_added = Projects.get_project(_link=_link)
        if len(project_added) > 0:
            Projects.query.filter_by(link=_link).delete()
            db.session.commit()
            print('deleted')
            return 'deleted'
        else:
            print('Project doesnt exist')
            return 'Project doesnt exist'

if __name__ == '__main__':
    #db.create_all()
    #print(Projects.get_project(_link='1'))
    #print(Projects.get_all_projects())
    #print(Projects.get_projects_for_course(_course_code='Math 352'))
    print(Projects.update_project(_link='1'))
    #print(Projects.delete_project(_link='1'))
    #print(Projects.add_projects(_name='00', _course_code='Math 351', _link='3'))