from sqlalchemy import ForeignKey, create_engine
from sqlalchemy.engine import URL
from sqlalchemy import Column, Integer, String, DateTime, Text
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
    admin_flag = Column(bool, default=False)
    login_attempts = Column(Integer, default=0)
    ttl = Column(DateTime(), default=datetime.now)

    def db_connect(self):
        url = URL.create(
            drivername="postgresql",
            username="postgres",
            password="test1234"
            host="localhost:5432",
            database="crux_db"
        )
        engine = create_engine(url)
        connection = engine.connect()
        Base.metadata.create_all(engine)

        Session = sessionmaker(bind=engine)
        return Session()
    
    def __init__(self, id, date, user_name, email, hash_pass, loginAttempts, ttl, admin=False):
        self.set_id = id
        self.set_date = date
        self.set_user_name(user_name)
        self.set_email(email)
        self.set_hash_pass(hash_pass)
        self.set_loginAttempts(loginAttempts)
        self.set_ttl(ttl)
        self.set_admin(admin)

    def set_user_name(self, user_name):
        self.user_name = user_name

    def set_email(self, email):
        self.email = email

    def set_hash_pass(self, hash_pass):
        self.hash_pass = hash_pass

    def set_loginAttempts(self, loginAttempts):
        self.loginAttempts = loginAttempts

    def set_ttl(self, ttl):
        self.ttl = ttl

    def set_admin(self, admin):
        self.admin = admin
    
    def set_id(self, id):
        self.id = id

    def set_date(self, date):
        self.date = date

    def create_user(self):
        pass
    
    def login_in_user(username, password):
        pass