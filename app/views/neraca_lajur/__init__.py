from app import server,db
from flask import render_template, request, redirect, url_for
from app.models.DaftarAkun import DaftarAkun
from app.models.NeracaLajur import NeracaLajur
from app.models.JurnalUmum import JurnalUmum
from sqlalchemy.sql import func
import random
import string



@server.route("/neraca-lajur")
def index_lajur():
    # daftar_akuns = NeracaLajur.query.order_by(NeracaLajur.id.desc())
    total_debit = db.session.query(func.sum(NeracaLajur.debit).label("total_debit")).scalar()
    total_credit = db.session.query(func.sum(NeracaLajur.credit).label("total_credit")).scalar()
    daftar_akuns = db.session.query( NeracaLajur.id, NeracaLajur.jenis,NeracaLajur.debit,NeracaLajur.credit, DaftarAkun.name.label('daftar_akun_name')).filter(NeracaLajur.daftar_akun_id == DaftarAkun.id).all()
    return render_template("neraca_lajur/index.html", title="Daftar Akun", daftar_akuns=daftar_akuns, total_credit=total_credit, total_debit=total_debit)

@server.route("/neraca-lajur/create", methods=['POST', 'GET'])
def create_lajur():
    if request.method == 'POST':
        daftar_akun_id = request.form['daftar_akun_id']
        # jenis = request.form['jenis']
        # debit = request.form['debit']
        # credit = request.form['credit']
        total = db.session.query(func.sum(JurnalUmum.deviation).label("total")).filter(JurnalUmum.daftar_akun_id == daftar_akun_id).scalar()
        print("$$$$$$$$$$$$")
        print(total)
        debit =0
        credit=0
        if total < 0:
            credit = abs(total)
        else:
            debit = total

        
        
        request_data = NeracaLajur( daftar_akun_id = daftar_akun_id, debit=debit, credit=credit)
        db.session.add(request_data)
        db.session.commit()
        return redirect(url_for('index_lajur'))
    daftar_akuns = DaftarAkun.query.all()
    return render_template("neraca_lajur/add.html", title="Daftar Akun", daftar_akuns=daftar_akuns)

@server.route("/neraca-lajur/edit/<id>", methods=['POST', 'GET'])
def edit_lajur(id):
    if  request.method == 'GET':
        data = NeracaLajur.query.get(int(id))
        daftar_akuns = DaftarAkun.query.all()
        return render_template("neraca_lajur/edit.html", title="Daftar Akun", data=data, daftar_akuns=daftar_akuns)
    if request.method == 'POST':
        daftar_akun_id = request.form['daftar_akun_id']
        debit = request.form['debit']
        credit = request.form['credit']
        
        db.session.query(NeracaLajur).filter(NeracaLajur.id == int(id)).update({
            'daftar_akun_id': daftar_akun_id,
            'debit': debit,
            'credit': credit
        })
        db.session.commit()
        return redirect(url_for('index_lajur'))
    
@server.route("/neraca-lajur/delete", methods=['POST'])
def delete_lajur():
    if  request.method == 'POST':
        id = request.form['id']
        if (id):
            NeracaLajur.query.filter_by(id=int(id)).delete()
            db.session.commit()
            return redirect(url_for('index_lajur'))


