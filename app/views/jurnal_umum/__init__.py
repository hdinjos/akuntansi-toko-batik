from app import server,db
from flask import render_template, request, redirect, url_for
from app.models.DaftarAkun import DaftarAkun
from app.models.JurnalUmum import JurnalUmum
from app.models.NeracaLajur import NeracaLajur
from sqlalchemy.sql import func
import random
import string



@server.route("/jurnal-umum")
def index_jurnal():
    # daftar_akuns = DaftarAkun.query.order_by(DaftarAkun.id.desc())
    daftar_akuns = db.session.query( JurnalUmum.id, JurnalUmum.date, JurnalUmum.date,JurnalUmum.note,JurnalUmum.debit,JurnalUmum.credit, DaftarAkun.name.label('daftar_akun_name')).filter(JurnalUmum.daftar_akun_id == DaftarAkun.id).all()
    return render_template("jurnal_umum/index.html", title="Daftar Akun", daftar_akuns=daftar_akuns)

@server.route("/jurnal-umum/create", methods=['POST', 'GET'])
def create_jurnal():
    if request.method == 'POST':
       
        date = request.form['date']
        daftar_akun_id = request.form['daftar_akun_id']
        note = request.form['note']
        debit = request.form['debit']
        credit = request.form['credit']
        deviation = float(debit)-float(credit)
        
        request_data = JurnalUmum(date=date, daftar_akun_id = daftar_akun_id, note=note, debit=debit, credit=credit, deviation=deviation)
        
        db.session.add(request_data)
        db.session.commit()
        total = db.session.query(func.sum(JurnalUmum.deviation).label("total")).filter(JurnalUmum.daftar_akun_id == daftar_akun_id).scalar()
        
        d =0
        c=0
        if total < 0:
            c = abs(total)
        else:
            d = total
        
        db.session.query(NeracaLajur).filter(NeracaLajur.daftar_akun_id == int(daftar_akun_id)).update({
            'debit': d,
            'credit': c
        })
        db.session.commit()
        return redirect(url_for('index_jurnal'))
    daftar_akuns = DaftarAkun.query.all()
    return render_template("jurnal_umum/add.html", title="Daftar Akun", daftar_akuns=daftar_akuns)

@server.route("/jurnal-umum/edit/<id>", methods=['POST', 'GET'])
def edit_jurnal(id):
    if  request.method == 'GET':
        data = JurnalUmum.query.get(int(id))
        daftar_akuns = DaftarAkun.query.all()
        return render_template("jurnal_umum/edit.html", title="Daftar Akun", data=data, daftar_akuns=daftar_akuns)
    if request.method == 'POST':
        date = request.form['date']
        daftar_akun_id = request.form['daftar_akun_id']
        note = request.form['note']
        debit = request.form['debit']
        credit = request.form['credit']
        deviation = float(debit)-float(credit)
        
        db.session.query(JurnalUmum).filter(JurnalUmum.id == int(id)).update({
            "date": date, "daftar_akun_id":daftar_akun_id, "note": note, "debit": debit, "credit": credit, "deviation": deviation
        })
        db.session.commit()
        
        total = db.session.query(func.sum(JurnalUmum.deviation).label("total")).filter(JurnalUmum.daftar_akun_id == daftar_akun_id).scalar()
        
        d =0
        c=0
        if total < 0:
            c = abs(total)
        else:
            d = total
        
        db.session.query(NeracaLajur).filter(NeracaLajur.daftar_akun_id == int(daftar_akun_id)).update({
            'debit': d,
            'credit': c
        })
        db.session.commit()
        return redirect(url_for('index_jurnal'))
    
@server.route("/jurnal-umum/delete", methods=['POST'])
def delete_jurnal():
    if  request.method == 'POST':
        id = request.form['id']
        if (id):
            find_id_daftar_akun = db.session.query(JurnalUmum.daftar_akun_id).filter_by(id=int(id)).scalar()
            print("PPPPP££££££")
            print(find_id_daftar_akun)
            
            JurnalUmum.query.filter_by(id=int(id)).delete()
            db.session.commit()
            
            total = db.session.query(func.sum(JurnalUmum.deviation).label("total")).filter(JurnalUmum.daftar_akun_id == int(find_id_daftar_akun)).scalar()
            print("PPPPP&&&&&^^&*&(*)")
            print(total)
            d =0
            c=0
            if total < 0:
                c = abs(total)
            else:
                d = total
            
            db.session.query(NeracaLajur).filter(NeracaLajur.daftar_akun_id == int(find_id_daftar_akun)).update({
                'debit': d,
                'credit': c
            })
            db.session.commit()
            return redirect(url_for('index_jurnal'))


