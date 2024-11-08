from app import server,db
from flask import render_template, request, redirect, url_for
from app.models.DaftarAkun import DaftarAkun
from app.models.NeracaLajur import NeracaLajur
import random
import string



@server.route("/neraca")
def index_neraca():
    daftar_akuns = db.session.query( NeracaLajur.id, NeracaLajur.jenis,NeracaLajur.debit,NeracaLajur.credit, DaftarAkun.name.label('daftar_akun_name')).filter(NeracaLajur.daftar_akun_id == DaftarAkun.id, NeracaLajur.jenis=='nrc').all()
    return render_template("neraca/index.html", title="Daftar Akun", daftar_akuns=daftar_akuns)


# @server.route("/neraca/create", methods=['POST', 'GET'])
# def create_neraca():
#     if request.method == 'POST':
#         random_string = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
#         code = random_string
#         name = request.form['name']
        
#         request_data = DaftarAkun(code=code, name=name)
#         db.session.add(request_data)
#         db.session.commit()
#         return redirect(url_for('index'))
#     return render_template("jurnal_umum/add.html", title="Daftar Akun")

# @server.route("/neraca/edit/<id>", methods=['POST', 'GET'])
# def edit_neraca(id):
#     if  request.method == 'GET':
#         data = DaftarAkun.query.get(int(id))
#         return render_template("jurnal_umum/edit.html", title="Daftar Akun", data=data)
#     if request.method == 'POST':
#         code = request.form['code']
#         name = request.form['name']
        
#         db.session.query(DaftarAkun).filter(DaftarAkun.id == int(id)).update({"code": code, "name": name})
#         db.session.commit()
#         return redirect(url_for('index'))
    
# @server.route("/neraca/delete", methods=['POST'])
# def delete_neraca():
#     if  request.method == 'POST':
#         id = request.form['id']
#         if (id):
#             DaftarAkun.query.filter_by(id=int(id)).delete()
#             db.session.commit()
#             return redirect(url_for('index'))


