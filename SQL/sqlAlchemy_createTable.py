from sqlalchemy import *
from sqlalchemy import create_engine, ForeignKey,PrimaryKeyConstraint
from sqlalchemy import  Column,Integer,String,Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref

def sqlSelector(softwareName,dbName):
    return create_engine(softwareName+":///"+dbName+".db",echo=True)

Base = declarative_base()

class Employee(Base):
    __tablename__ = "employee"
    """
    declare all column details
    """
    eid = Column(Integer,primary_key=True)
    UserName = Column(String)
    FirstName = Column(String)
    LastName = Column(String)
    position = Column(String)
    dateJoined = Column(Date)

    def __init__(self,*args):   
       print(args)
       self.UserName,self.FirstName,self.LastName,self.position,self.dateJoined = args     

engine = sqlSelector("sqlite","employeeDb")
Base.metadata.create_all(engine) 



