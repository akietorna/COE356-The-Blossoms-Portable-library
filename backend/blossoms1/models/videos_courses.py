from models.courses_model import *
from models.videos_model import *

# the class Movie will inherit the db.Model of SQLAlchemy


class Videos_courses(db.Model):
    __tablename__ = 'videos_courses'  # creating a table name
    id = db.Column(db.Integer, primary_key=True)  # this is the primary key
    link = db.Column(db.String(500), nullable=False)  # todo foreign key
    # nullable is false so the column can't be empty
    course_code = db.Column(db.String(10), nullable=False)  # todo foreign key

    def json_videos_courses(self):
        return {'id': self.id,
                'link': self.link,
                'course_code': self.course_code}
        # this method we are defining will convert our output to json

    def add_video_course(_link, _course_code):
        new_vid_course = Videos_courses(link=_link, course_code=_course_code)

        course_exists = Courses.get_course(_code=_course_code)
        print(course_exists)
        vid_exists = Videos.get_video(_link=_link)
        print(vid_exists)

        if len(course_exists) > 0 and len(vid_exists) > 0:
            vid_course_already_added = Videos_courses.get_vid_course_rel(
                _link=_link, _course_code=_course_code)

            if len(vid_course_already_added) > 0:
                return 'Video Course relationship already exists'
            db.session.add(new_vid_course)
            db.session.commit()
            print('Video Course relation added')
            return 'Video Course relation added'
        else:
            return 'Either of Video or Course doesnt exist, check it out'

    def get_all_vid_courses(i=None):
        return [Videos_courses.json_videos_courses(item) for item in Videos_courses.query.all()]

    def get_vids_for_course(_course_code):
        result = Videos_courses.query.filter_by(course_code=_course_code).all()
        print(result)
        if result == None:
            return []
        return [Videos_courses.json_videos_courses(slide) for slide in result]

    def get_vid_course_rel(_link, _course_code):
        result = Videos_courses.query.filter_by(
            course_code=_course_code, link=_link).first()
        print(result)
        if result == None:
            return []
        return [Videos_courses.json_videos_courses(result)]

    def update_vid_course(_link, _new_link, _code, _new_code=None):
        vid_course_added = Videos_courses.get_vid_course_rel(
            _link=_link, _course_code=_code)
        if len(vid_course_added) > 0:
            vid_course_to_update = Videos_courses.query.filter_by(
                link=_link, course_code=_code).first()
            vid_course_to_update.link = _new_link
            if _code == None:
                pass
            else:
                vid_course_to_update.course_code = _new_code
            db.session.commit()
            print('updated')
            return 'updated'
        else:
            return 'Video_course relation doesnt exist'

    def delete_vid_course(_link, _course):
        vid_cousrse_added = Videos_courses.get_vid_course_rel(
            _link=_link, _course_code=_course)
        if len(vid_cousrse_added) > 0:
            Videos_courses.query.filter_by(
                link=_link, course_code=_course).delete()
            db.session.commit()
            print('deleted')
            return 'deleted'
        else:
            print('Video Course relation doesnt exist')


if __name__ == '__main__':
    # db.create_all()
    #Videos_courses.delete_vid_course(_link='1', _course='Math 351')
    print(Videos_courses.add_video_course(_link='1', _course_code='Math 351'))
    # print(Videos_courses.get_all_vid_courses())
