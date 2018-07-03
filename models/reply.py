from models.user import User
from sqlalchemy import (
    Column,
    String,
    INTEGER,

)

from models import (
    SQLMixin,
    SQLBase,
)

class Reply(SQLMixin, SQLBase):
    __tablename__ = 'Reply'

    content = Column(String(2000), nullable=False)
    topic_id = Column(INTEGER, nullable=False)
    user_id = Column(INTEGER, nullable=False)

    def user(self):
        u = User.one(self.user_id)
        return u

