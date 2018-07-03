from sqlalchemy import (
    Column,
    String,
    INTEGER,
)

from models import (
    SQLMixin,
    SQLBase,
)


class Mail(SQLMixin, SQLBase):
    __tablename__ = 'Mail'
    title = Column(String(50), nullable=False)
    content = Column(String(200), nullable=False)
    sender_id = Column(INTEGER, nullable=False)
    receiver_id = Column(INTEGER, nullable=False)


