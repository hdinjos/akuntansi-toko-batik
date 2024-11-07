from app.models import db
from app.models.JurnalUmum import JurnalUmum
from app.models.NeracaLajur import NeracaLajur
# from app.models import Scrapped


class KategoriDaftarAkun(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name= db.Column(db.String(200), unique=False, nullable=False)
  daftar_akun= db.relationship('DaftarAkun', backref='kategori_daftar_akun', passive_deletes=True)

class DaftarAkun(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  code= db.Column(db.String(5), unique=False, nullable=False)
  name= db.Column(db.String(200), unique=False, nullable=False)
  category_id=db.Column(db.Integer, db.ForeignKey('kategori_daftar_akun.id', ondelete='CASCADE'))
  jurnal_umum= db.relationship('JurnalUmum', backref='daftar_akun', passive_deletes=True)
  naraca_lajur= db.relationship('NeracaLajur', backref='daftar_akun', passive_deletes=True)
  