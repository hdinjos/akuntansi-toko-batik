from app import server,db
from flask import render_template, request, redirect, url_for
from app.models.DaftarAkun import DaftarAkun
import random
import string



@server.route("/jurnal-umum")
def index_jurnal():
    daftar_akuns = DaftarAkun.query.order_by(DaftarAkun.id.desc())
    return render_template("jurnal_umum/index.html", title="Daftar Akun", daftar_akuns=daftar_akuns)

@server.route("/jurnal-umum/create", methods=['POST', 'GET'])
def create_jurnal():
    if request.method == 'POST':
        random_string = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
        code = random_string
        name = request.form['name']
        
        request_data = DaftarAkun(code=code, name=name)
        db.session.add(request_data)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template("jurnal_umum/add.html", title="Daftar Akun")

@server.route("/jurnal-umum/edit/<id>", methods=['POST', 'GET'])
def edit_jurnal(id):
    if  request.method == 'GET':
        data = DaftarAkun.query.get(int(id))
        return render_template("jurnal_umum/edit.html", title="Daftar Akun", data=data)
    if request.method == 'POST':
        code = request.form['code']
        name = request.form['name']
        
        db.session.query(DaftarAkun).filter(DaftarAkun.id == int(id)).update({"code": code, "name": name})
        db.session.commit()
        return redirect(url_for('index'))
    
@server.route("/jurnal-umum/delete", methods=['POST'])
def delete_jurnal():
    if  request.method == 'POST':
        id = request.form['id']
        if (id):
            DaftarAkun.query.filter_by(id=int(id)).delete()
            db.session.commit()
            return redirect(url_for('index'))


