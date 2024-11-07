from app.models import db
# from app.models.DaftarAkun import DaftarAkun
# from app.models import Scrapped

class NeracaLajur(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  jenis= db.Column(db.String(5), unique=False, nullable=False)
  debit= db.Column(db.Float, unique=False, nullable=False, default=0)
  credit= db.Column(db.Float, unique=False, nullable=False, default=0)
  daftar_akun_id=db.Column(db.Integer, db.ForeignKey('daftar_akun.id', ondelete='CASCADE'))