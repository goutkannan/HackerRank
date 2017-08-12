
from sqlalchemy.orm import sessionmaker
from sqlAlchemy_createTable import Employee, sqlSelector
 
engine = sqlSelector("sqlite", "employeeDb")

_Session = sessionmaker(bind=engine )
currentSesion = _Session()

for emp in currentSesion.query(Employee).order_by(Employee.eid):
    print(emp)
