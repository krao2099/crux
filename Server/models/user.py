from sqlalchemy import ForeignKey, create_engine
from sqlalchemy.engine import URL
from sqlalchemy import Column, Integer, String, DateTime, Boolean
from sqlalchemy.orm import declarative_base
from datetime import datetime
from sqlalchemy.orm import relationship, backref
from sqlalchemy.orm import sessionmaker

Base = declarative_base()
class user(Base):
    __tablename__ = 'Users'
    id = Column(Integer(), primary_key=True)
    creation_date = Column(DateTime(), default=datetime.now)
    username = Column(String(50), nullable=False, unique=True)
    email = Column(String(254), nullable=False, unique=True)
    hash_password = Column(String(65534), nullable=False)
    admin_flag = Column(Boolean, default=False)
    login_attempts = Column(Integer, default=0)
    ttl = Column(DateTime(), default=datetime.now)

    def db_connect(self):
        url = URL.create(
            drivername="postgresql",
            username="postgres",
            password="test1234",
            host="localhost:5432",
            database="crux_db"
        )
        engine = create_engine(url)
        connection = engine.connect()

        Session = sessionmaker(bind=engine)
        return Session()
    
    def __init__(self, id, date, username, email, hash_password, login_attempts, ttl, admin_flag=False):
        self.set_id = id
        self.set_creation_date = date
        self.set_username(username)
        self.set_email(email)
        self.set_hash_password(hash_password)
        self.set_login_attempts(login_attempts)
        self.set_ttl(ttl)
        self.set_admin_flag(admin_flag)

    def set_username(self, username):
        self.username = username

    def set_email(self, email):
        self.email = email

    def set_hash_password(self, hash_password):
        self.hash_password = hash_password

    def set_login_attempts(self, login_attempts):
        self.login_attempts = login_attempts

    def set_ttl(self, ttl):
        self.ttl = ttl

    def set_admin_flag(self, admin_flag):
        self.admin_flag = admin_flag
    
    def set_id(self, id):
        self.id = id

    def set_date(self, date):
        self.date = date

    def create_user(self):
        session = self.db_connect()
        session.add(user)
        session.commit()
        session.close()
    
    def login_in_user(username, password):
        pass