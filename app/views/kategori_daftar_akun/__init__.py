from app import server,db
from flask import render_template, request, redirect, url_for
from app.models.DaftarAkun import KategoriDaftarAkun
import random
import string



@server.route("/daftar-akun-cat")
def index_cat():
    daftar_akuns = KategoriDaftarAkun.query.order_by(KategoriDaftarAkun.id.desc())
    return render_template("kategori_daftar_akun/index.html", title="Daftar Akun", daftar_akuns=daftar_akuns)

@server.route("/daftar-akun-cat/create", methods=['POST', 'GET'])
def create_cat():
    if request.method == 'POST':
        name = request.form['name']
        
        request_data = KategoriDaftarAkun(name=name)
        db.session.add(request_data)
        db.session.commit()
        return redirect(url_for('index_cat'))
    return render_template("kategori_daftar_akun/add.html", title="Daftar Akun")

@server.route("/daftar-akun-cat/edit/<id>", methods=['POST', 'GET'])
def edit_cat(id):
    if  request.method == 'GET':
        data = KategoriDaftarAkun.query.get(int(id))
        return render_template("kategori_daftar_akun/edit.html", title="Daftar Akun", data=data)
    if request.method == 'POST':
        name = request.form['name']
        
        db.session.query(KategoriDaftarAkun).filter(KategoriDaftarAkun.id == int(id)).update({"name": name})
        db.session.commit()
        return redirect(url_for('index_cat'))
    
@server.route("/daftar-akun-cat/delete", methods=['POST'])
def delete_cat():
    if  request.method == 'POST':
        id = request.form['id']
        if (id):
            KategoriDaftarAkun.query.filter_by(id=int(id)).delete()
            db.session.commit()
            return redirect(url_for('index_cat'))


