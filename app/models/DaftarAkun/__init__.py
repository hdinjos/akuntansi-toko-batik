from app.models import db
# from app.models import Scrapped

class DaftarAkun(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  code= db.Column(db.String(5), unique=False, nullable=False)
  name= db.Column(db.String(20), unique=False, nullable=False)
  category_id= db.Column(db.Integer, unique=False, nullable=True)