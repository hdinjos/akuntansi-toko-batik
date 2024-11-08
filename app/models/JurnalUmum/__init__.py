from app.models import db
# from app.models.DaftarAkun import DaftarAkun
# from app.models import Scrapped

class JurnalUmum(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  date= db.Column(db.Date, unique=False, nullable=False)
  note= db.Column(db.Text, unique=False, nullable=False)
  debit= db.Column(db.Float, unique=False, nullable=False, default=0)
  credit= db.Column(db.Float, unique=False, nullable=False, default=0)
  deviation= db.Column(db.Float, unique=False, nullable=False, default=0)
  daftar_akun_id=db.Column(db.Integer, db.ForeignKey('daftar_akun.id', ondelete='CASCADE'))