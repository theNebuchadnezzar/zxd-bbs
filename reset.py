from sqlalchemy import Column, String

from models import (
    reset_database,
    SQLMixin,
    SQLBase,
)
from models.user import User
from models.topic import Topic
from models.reply import Reply
from models.board import Board
from models.mail import Mail


from utils import log


class Test(SQLMixin, SQLBase):
    __tablename__ = 'Test'
    username = Column(String(20), nullable=False)


def main():
    reset_database()

    # t = Test.new(
    #     username='test username'
    # )
    # log('t.username', t)

    # t.username
    # log('t.username', t.username)
    # Test.usrename
    #
    User.new(
        username='zxd',
        password='123',
    )

    User.new(
        username='test',
        password='123',
    )
    print(User.exist(id=1))
    print(User.exist(id=3))
    #
    # # Topic.new(
    #     title='Topic test01',
    #     content='Topic test01',
    #     user_id=1,
    # )

    # Reply.new(
    #     content='Reply test01',
    #     topic_id=1,
    #     user_id=1,
    # )
    #
    # Mail.new(
    #     title='Mail test01',
    #     content='Mail test01',
    #     sender_id=2,
    #     receiver_id=2,
    # )
    # Board.new(
    #     title='Board test01',
    # )


if __name__ == '__main__':
    main()
