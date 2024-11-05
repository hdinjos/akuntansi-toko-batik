from app import server,db
from flask import render_template, request, redirect, url_for
from app.models.DaftarAkun import DaftarAkun

@server.route("/")
def index():
    daftar_akuns = DaftarAkun.query.order_by(DaftarAkun.id.desc())
    return render_template("daftar_akun/index.html", title="Daftar Akun", daftar_akuns=daftar_akuns)

@server.route("/daftar-akun/create", methods=['POST', 'GET'])
def create():
    if request.method == 'POST':
        code = request.form['code']
        name = request.form['name']
        
        request_data = DaftarAkun(code=code, name=name)
        db.session.add(request_data)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template("daftar_akun/add.html", title="Daftar Akun")

@server.route("/daftar-akun/edit/<id>", methods=['POST', 'GET'])
def edit(id):
    if  request.method == 'GET':
        data = DaftarAkun.query.get(int(id))
        return render_template("daftar_akun/edit.html", title="Daftar Akun", data=data)
    if request.method == 'POST':
        code = request.form['code']
        name = request.form['name']
        
        db.session.query(DaftarAkun).filter(DaftarAkun.id == int(id)).update({"code": code, "name": name})
        db.session.commit()
        return redirect(url_for('index'))
    
@server.route("/daftar-akun/delete", methods=['POST'])
def delete():
    if  request.method == 'POST':
        id = request.form['id']
        if (id):
            DaftarAkun.query.filter_by(id=int(id)).delete()
            db.session.commit()
            return redirect(url_for('index'))


