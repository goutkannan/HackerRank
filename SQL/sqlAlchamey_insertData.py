import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlAlchemy_createTable import Employee,sqlSelector

"""
Use the exisiting engine object and try 

Create a new session and bind the engine object
"""
engine = sqlSelector("sqlite","employeeDb")
_Session = sessionmaker(bind=engine )

currentSesion = _Session()

empDetail = Employee("gout.kannan","Goutham","Kannan","SDE 1","08/09/2017")
currentSesion.add(empDetail)

empDetail = Employee("gkannan1","Goutham","Kannan","SDE 2","03/09/2016")
currentSesion.add(empDetail)

empDetail = Employee("diglika","Mahtoug","Nannak","1 SE","12/2/2012")
currentSesion.add(empDetail)


currentSesion.commit()


#   To Test if the data is saved 




