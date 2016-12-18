from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
 
metadata = MetaData()

user = Table('user', metadata,
    Column('user_id', Integer, primary_key=True),
    Column('user_name', String(16), nullable=False),
    Column('email_address', String, key='email'),
    Column('password', String(20), nullable=False)
)

SQLmetadata.create_all(engine)

'''
Base = declarative_base()

class Appuser(Base):
    __tablename__ = 'appuser'
    appuser_id = Column(Integer, primary_key=True)
    user_name = Column(String, nullable=False)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    password = Column(String, nullable=False)
    email = Column(String, nullable=False)
    privilege = Column(Integer, default=0)


class Service():
	def __init__(self,engine):
		self.engine = engine
		# for more detail see. http://docs.sqlalchemy.org/en/latest/orm/session_basics.html 
		self._Session = sessionmaker(bind=self.engine)

	def get(self):		
		pass
	def delete(self):
		pass
	def post(self,appuser_inst,autocommit=True):
		session = self._Session()
		session.add(appuser_inst)
		session.commit()
'''
		pass
	def patch(self):
		session = self._Session()
		session.add(appuser_inst)
		session.commit()
		pass
	def search(self):
		pass