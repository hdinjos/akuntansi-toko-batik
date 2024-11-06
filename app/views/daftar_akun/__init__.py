from app import server,db
from flask import render_template, request, redirect, url_for
from app.models.DaftarAkun import DaftarAkun, KategoriDaftarAkun
import random
import string


@server.route("/")
def index():
    # daftar_akuns = DaftarAkun.query.all()
    daftar_akuns = db.session.query( DaftarAkun.id, DaftarAkun.code, DaftarAkun.name, KategoriDaftarAkun.name.label('category_name')).filter(DaftarAkun.category_id == KategoriDaftarAkun.id).all()

    return render_template("daftar_akun/index.html", title="Daftar Akun", daftar_akuns=daftar_akuns)

@server.route("/daftar-akun/create", methods=['POST', 'GET'])
def create():
    if request.method == 'POST':
        random_string = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
        code = random_string
        name = request.form['name']
        category_id = request.form['category_id']
        
        request_data = DaftarAkun(code=code, name=name, category_id=category_id)
        db.session.add(request_data)
        db.session.commit()
        return redirect(url_for('index'))
    
    kategoris = KategoriDaftarAkun.query.order_by(KategoriDaftarAkun.id.desc())
    return render_template("daftar_akun/add.html", title="Daftar Akun", kategoris=kategoris)

@server.route("/daftar-akun/edit/<id>", methods=['POST', 'GET'])
def edit(id):
    if  request.method == 'GET':
        data = DaftarAkun.query.get(int(id))
        kategoris = KategoriDaftarAkun.query.order_by(KategoriDaftarAkun.id.desc())
        return render_template("daftar_akun/edit.html", title="Daftar Akun", data=data, kategoris=kategoris)
    if request.method == 'POST':
        code = request.form['code']
        name = request.form['name']
        category_id = int(request.form['category_id'])
        
        db.session.query(DaftarAkun).filter(DaftarAkun.id == int(id)).update({"code": code, "name": name, "category_id":category_id})
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


