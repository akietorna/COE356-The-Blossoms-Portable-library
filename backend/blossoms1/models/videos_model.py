from backend.blossoms1.settings import *


# the class Movie will inherit the db.Model of SQLAlchemy
class Videos(db.Model):
    __tablename__ = 'videos'  # creating a table name
    id = db.Column(db.Integer, primary_key=True)  # this is the primary key
    name = db.Column(db.String(200), nullable=True)
    link = db.Column(db.String(500), nullable=False)
    # nullable is false so the column can't be empty
    creator = db.Column(db.String(100), nullable=True)

    def json_videos(self):
        return {
            'name': self.name,
            'link': self.link,
            'creator': self.creator
        }

    def add_video(_name, _link, _creator=' '):
        new_video = Videos(name=_name, link=_link, creator=_creator)
        db.session.add(new_video)
        db.session.commit()

    def get_all_videos(i=None):
        return [Videos.json_videos(vid) for vid in Videos.query.all()]

    def get_video(_link):
        result = Videos.query.filter_by(link=_link).first()
        print(result)
        if result == None:
            return []
        return [Videos.json_videos(result)]

    def update_video(_name, _link, _creator):
        video_to_update = Videos.query.filter_by(link=_link).first()
        if _name != None:
            video_to_update.name = _name
        if _creator != None:
            video_to_update.creator = _creator
        db.session.commit()

    def delete_video(_link):
        Videos.query.filter_by(link=_link).delete()
        db.session.commit()


if __name__ == '__main__':
    db.create_all()
