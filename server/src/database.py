import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


host = os.getenv("MARIADB_HOST")
port = os.getenv("MARIADB_PORT")
name = os.getenv("MARIADB_USER")
password = os.getenv("MARIADB_PASSWORD")
db = os.getenv("MARIADB_DB")

mariadb_url = f"mysql+pymysql://{name}:{password}@{host}:{port}/{db}"

engine = create_engine(mariadb_url)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()