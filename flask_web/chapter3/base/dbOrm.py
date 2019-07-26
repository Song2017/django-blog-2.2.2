# coding=utf-8
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy import and_, or_
from db_consts import DB_URI

eng = create_engine(DB_URI)
Base = declarative_base()


# orm
class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50))


class Address(Base):
    __tablename__ = 'address'
    id = Column(Integer, primary_key=True, autoincrement=True)
    email_address = Column(String(128), nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship('User', back_populates='addresses')


# join
User.addresses = relationship(
    'Address', order_by=Address.id, back_populates='user')
Base.metadata.drop_all(bind=eng)
Base.metadata.create_all(bind=eng)

Session = sessionmaker(bind=eng)
session = Session()

user = User(name='xiaoming')

user.addresses = [Address(email_address='a@gmail.com', user_id=user.id),
                  Address(email_address='b@gmail.com', user_id=user.id)]
session.add(user)
session.commit()

session.add_all(
    [User(name=username) for username in ('xiaoming', 'wanglang', 'lilei')])

session.commit()


def get_result(rs):
    print('-' * 20)
    print(rs)
    for user in rs:
        print(user.name)


rs = session.query(User).all()
get_result(rs)
rs = session.query(User).filter(User.id.in_([
    2,
]))
get_result(rs)
rs = session.query(User).filter(and_(User.id > 2, User.id < 4))
get_result(rs)
rs = session.query(User).filter(or_(User.id == 2, User.id == 4))
get_result(rs)
rs = session.query(User).filter(User.name.like('%min%'))
get_result(rs)
user = session.query(User).filter_by(name='xiaoming').first()
get_result([user])
