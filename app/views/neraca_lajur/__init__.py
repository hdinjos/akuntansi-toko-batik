from app import server,db
from flask import render_template, request, redirect, url_for
from app.models.DaftarAkun import DaftarAkun
from app.models.NeracaLajur import NeracaLajur
import random
import string



@server.route("/neraca-lajur")
def index_lajur():
    # daftar_akuns = NeracaLajur.query.order_by(NeracaLajur.id.desc())
    
    daftar_akuns = db.session.query( NeracaLajur.id, NeracaLajur.jenis,NeracaLajur.debit,NeracaLajur.credit, DaftarAkun.name.label('daftar_akun_name')).filter(NeracaLajur.daftar_akun_id == DaftarAkun.id).all()
    return render_template("neraca_lajur/index.html", title="Daftar Akun", daftar_akuns=daftar_akuns)

@server.route("/neraca-lajur/create", methods=['POST', 'GET'])
def create_lajur():
    if request.method == 'POST':
        daftar_akun_id = request.form['daftar_akun_id']
        jenis = request.form['jenis']
        debit = request.form['debit']
        credit = request.form['credit']
        
        request_data = NeracaLajur( daftar_akun_id = daftar_akun_id, jenis=jenis, debit=debit, credit=credit)
        db.session.add(request_data)
        db.session.commit()
        return redirect(url_for('index_lajur'))
    daftar_akuns = DaftarAkun.query.all()
    return render_template("neraca_lajur/add.html", title="Daftar Akun", daftar_akuns=daftar_akuns)

@server.route("/neraca-lajur/edit/<id>", methods=['POST', 'GET'])
def edit_lajur(id):
    if  request.method == 'GET':
        data = DaftarAkun.query.get(int(id))
        return render_template("neraca_lajur/edit.html", title="Daftar Akun", data=data)
    if request.method == 'POST':
        code = request.form['code']
        name = request.form['name']
        
        db.session.query(DaftarAkun).filter(DaftarAkun.id == int(id)).update({"code": code, "name": name})
        db.session.commit()
        return redirect(url_for('index_lajur'))
    
@server.route("/neraca-lajur/delete", methods=['POST'])
def delete_lajur():
    if  request.method == 'POST':
        id = request.form['id']
        if (id):
            DaftarAkun.query.filter_by(id=int(id)).delete()
            db.session.commit()
            return redirect(url_for('index_lajur'))


