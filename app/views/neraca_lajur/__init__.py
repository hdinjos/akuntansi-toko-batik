from app import server,db
from flask import render_template, request, redirect, url_for
from app.models.DaftarAkun import DaftarAkun
import random
import string



@server.route("/neraca-lajur")
def index_lajur():
    daftar_akuns = DaftarAkun.query.order_by(DaftarAkun.id.desc())
    return render_template("jurnal_umum/index.html", title="Daftar Akun", daftar_akuns=daftar_akuns)

@server.route("/neraca-lajur/create", methods=['POST', 'GET'])
def create_lajur():
    if request.method == 'POST':
        random_string = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
        code = random_string
        name = request.form['name']
        
        request_data = DaftarAkun(code=code, name=name)
        db.session.add(request_data)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template("jurnal_umum/add.html", title="Daftar Akun")

@server.route("/neraca-lajur/edit/<id>", methods=['POST', 'GET'])
def edit_lajur(id):
    if  request.method == 'GET':
        data = DaftarAkun.query.get(int(id))
        return render_template("jurnal_umum/edit.html", title="Daftar Akun", data=data)
    if request.method == 'POST':
        code = request.form['code']
        name = request.form['name']
        
        db.session.query(DaftarAkun).filter(DaftarAkun.id == int(id)).update({"code": code, "name": name})
        db.session.commit()
        return redirect(url_for('index'))
    
@server.route("/neraca-lajur/delete", methods=['POST'])
def delete_lajur():
    if  request.method == 'POST':
        id = request.form['id']
        if (id):
            DaftarAkun.query.filter_by(id=int(id)).delete()
            db.session.commit()
            return redirect(url_for('index'))


