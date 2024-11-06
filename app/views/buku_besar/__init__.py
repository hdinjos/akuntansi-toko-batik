from app import server,db
from flask import render_template, request, redirect, url_for
from app.models.DaftarAkun import DaftarAkun
from app.models.JurnalUmum import JurnalUmum
import random
import string
from itertools import groupby



@server.route("/buku-besar")
def index_buku():
    # daftar_akuns = DaftarAkun.query.order_by(DaftarAkun.id.desc())
    jurnal_umums = db.session.query( JurnalUmum.id, JurnalUmum.date, JurnalUmum.date,JurnalUmum.note,JurnalUmum.debit,JurnalUmum.credit, DaftarAkun.id.label('daftar_akun_id'), DaftarAkun.name.label('daftar_akun_name'), DaftarAkun.code.label('code')).filter(JurnalUmum.daftar_akun_id == DaftarAkun.id).all()
    
    # Step 1: Sort the list by 'by' field to ensure groupby works properly
    sorted_lists = sorted(jurnal_umums, key=lambda x: x.daftar_akun_name)

    # Step 2: Group the sorted list by 'by' field
    grouped = groupby(sorted_lists, key=lambda x: x.daftar_akun_name +" (" + x.code +")")

    # # Step 3: Format the result
    datas = []
    for key, group in grouped:
        ingroup = []
        datas.append({"daftar_akun_name":key, "daftar": ingroup})
        balance = 0
        for item in group:
            balance+= item.debit
            balance-= item.credit
            ingroup.append({ "date": item.date, "note": item.note, "debit": item.debit, "credit": item.credit, "balance": balance})

    return render_template("buku_besar/index.html", title="Daftar Akun", buku_besar=datas)

# @server.route("/buku-besar/create", methods=['POST', 'GET'])
# def create_buku():
#     if request.method == 'POST':
#         random_string = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
#         code = random_string
#         name = request.form['name']
        
#         request_data = DaftarAkun(code=code, name=name)
#         db.session.add(request_data)
#         db.session.commit()
#         return redirect(url_for('index'))
#     return render_template("jurnal_umum/add.html", title="Daftar Akun")

# @server.route("/daftar-akun/edit/<id>", methods=['POST', 'GET'])
# def edit_buku(id):
#     if  request.method == 'GET':
#         data = DaftarAkun.query.get(int(id))
#         return render_template("jurnal_umum/edit.html", title="Daftar Akun", data=data)
#     if request.method == 'POST':
#         code = request.form['code']
#         name = request.form['name']
        
#         db.session.query(DaftarAkun).filter(DaftarAkun.id == int(id)).update({"code": code, "name": name})
#         db.session.commit()
#         return redirect(url_for('index'))
    
# @server.route("/buku-besar/delete", methods=['POST'])
# def delete_buku():
#     if  request.method == 'POST':
#         id = request.form['id']
#         if (id):
#             DaftarAkun.query.filter_by(id=int(id)).delete()
#             db.session.commit()
#             return redirect(url_for('index'))


