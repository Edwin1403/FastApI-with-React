from sqlalchemy import Column, String,Integer,TIMESTAMP,text,ForeignKey,Date
from .database import base
from sqlalchemy.orm import relationship



class user(base):
    __tablename__="Users"
    id=Column(Integer,primary_key=True,nullable=False,index = True)
    fullname= Column(String,nullable=False, index=True)
    email=Column(String,nullable=False, index=True)
    password=Column(String,nullable=False)
    dob=Column(Date, nullable=False, index=True)
    contactnumber =Column(String,nullable=False, index=True)
    gender = Column(String, nullable=False,index=True)
    selectcourse=Column(String, nullable=False,index=True)
    reason= Column(String, nullable=False, index=True)
    created_at=Column(TIMESTAMP,nullable=False,server_default=text('now()'))


class Post(base):
    __tablename__ = "Post"
    id=Column(Integer , primary_key=True , nullable=False)
    owner_id = Column(Integer , ForeignKey("Users.id" , ondelete='CASCADE') , nullable=False)
    title=Column(String , nullable=True)
    content = Column(String , nullable=True)

    owner = relationship("user")

class Vote(base):
    __tablename__ = "vote"
    user_id = Column(Integer , ForeignKey('Users.id' , ondelete='CASCADE') , nullable=False , primary_key = True)
    post_id = Column(Integer , ForeignKey('Post.id' , ondelete='CASCADE') , nullable = False , primary_key = True)    