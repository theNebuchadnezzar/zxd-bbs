import hashlib

from sqlalchemy import Column, String

from models import (
    SQLMixin,
    SQLBase,
)
from utils import log

class User(SQLMixin, SQLBase):
    __tablename__ = 'User'
    """
    User 是一个保存用户数据的 model
    现在只有两个属性 username 和 password
    """

    username = Column(String(50), nullable=False)
    password = Column(String(100), nullable=False)
    image = Column(String(100), nullable=False, default='/images/default.gif')
    signature = Column(String(100), nullable=False, default='Hello,world!')


    def add_default_value(self):
        super().add_default_value()
        self.password = self.salted_password(self.password)

    @staticmethod
    def salted_password(password, salt='$!@><?>HUI&DWQa`'):
        salted = hashlib.sha256((password + salt).encode('ascii')).hexdigest()
        return salted

    @classmethod
    def register(cls, form):
        name = form.get('username', '')
        pwd = form.get('password', '')
        if len(name) > 2 and not User.exist(username=name):
            # 错误，只应该 commit 一次
            # u = User.new(**form)
            # u.password = u.salted_password(pwd)
            # User.session.add(u)
            # User.session.commit()
            u = User.new(**form)
            return u
        else:
            return None

    @classmethod
    def validate_login(cls, form):
        query = dict(
            username=form['username'],
            password=User.salted_password(form['password']),
        )
        log('query ', query)
        e = User.exist(**query)
        log(e)
        if e:
            return User.one(**query)
        else:
            return None


    def recent_replied_topics(self, user_id):
        from models.reply import Reply
        from models.topic import Topic

        replies = Reply.all(user_id=user_id)
        #对replies排序
        replies.sort(key=lambda reply: reply.created_time, reverse=True)
        print('replies reversed ', replies)

        #按照顺序找到对应的topic_id
        topics_id = [reply.topic_id for reply in replies]

        #去重
        topics_sorted_id = []
        for t in topics_id:
            if t not in topics_sorted_id:
                topics_sorted_id.append(t)

        print('topics_sorted reversed ', topics_sorted_id)

        #按照顺序找到topic_id对应的topic对象
        topics_sorted = [Topic.one(id=id) for id in topics_sorted_id]

        return topics_sorted


    def recent_created_topics(self, user_id):
        from models.topic import Topic

        topics = Topic.all(user_id=user_id)
        print('topics reversed  recent_created_topics ', topics)

        topics.sort(key=lambda topic: topic.created_time, reverse=True)
        print('topics reversed recent_created_topics sort ', topics)

        return topics
