from backend.blossoms1.settings import *

# the class Movie will inherit the db.Model of SQLAlchemy


class Programs(db.Model):
    __tablename__ = 'programs'  # creating a table name
    id = db.Column(db.Integer, primary_key=True)  # this is the primary key
    name = db.Column(db.String(80), nullable=False)
    # nullable is false so the column can't be empty
    about = db.Column(db.String(1000), nullable=True)
    department = db.Column(db.String(100), nullable=True)

    def json_programs(self):
        return {
            'name': self.name,
            'about': self.about,
            'department': self.department
        }

    def add_program(_name, _about, _department=' '):
        new_program = Programs(name=_name, about=_about,
                               department=_department)
        db.session.add(new_program)
        db.session.commit()

    def get_all_programs(i=None):
        return [Programs.json_programs(program) for program in Programs.query.all()]

    def get_program(_name):
        result = Programs.query.filter_by(name=_name).first()
        print(result)
        if result == None:
            return []
        return [Programs.json_programs(result)]

    def update_program(_name, _about=None, _department=None):
        program_to_update = Programs.query.filter_by(name=_name).first()
        program_to_update.name = _name
        if _about != None:
            program_to_update.about = _about
        if _department != None:
            program_to_update.department = _department
        db.session.commit()

    def delete_program(_name):
        Programs.query.filter_by(name=_name).delete()
        db.session.commit()


if __name__ == '__main__':
    db.create_all()
