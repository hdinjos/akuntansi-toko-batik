from flask import Flask
from flask_migrate import Migrate

server = Flask(__name__)
server.secret_key = "j(A#@#UWEJ(AEJ"
server.debug = True
server.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:root@127.0.0.1:8889/toko_batik"

from app.models import db

migrate = Migrate(server, db)

# from app.views import Home, Load_Data, Data_Scrapped, Preprocessing, Calculate
from app.views import daftar_akun, jurnal_umum, buku_besar, neraca_lajur, laba_rugi, neraca, kategori_daftar_akun