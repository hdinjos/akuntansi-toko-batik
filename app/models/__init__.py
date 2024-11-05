# from app import db
from app import server
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy(server)