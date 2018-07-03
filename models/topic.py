import time
from models import Model

from models.user import User
from models.reply import Reply
from sqlalchemy import (
    Column,
    String,
    INTEGER,
)

from models import (
    SQLMixin,
    SQLBase,
)

class Topic(SQLMixin, SQLBase):
    __tablename__ = 'Topic'

    title = Column(String(50), nullable=False)
    content = Column(String(2000), nullable=False)
    views = Column(INTEGER, nullable=False, default='0')
    user_id = Column(INTEGER, nullable=False)


    @classmethod
    def get(cls, id):
        m = cls.one(id=id)
        m.views += 1
        Topic.session.add(m)
        Topic.session.commit()
        return m



    def user(self):
        u = User.one(self.user_id)
        return u

    def replies(self):
        ms = Reply.all(topic_id=self.id)
        return ms

    def reply_count(self):
        count = len(self.replies())
        return count

