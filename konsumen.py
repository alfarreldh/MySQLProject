from flask import Flask, render_template, request, abort, make_response, jsonify, json
from flask.wrappers import Response
from flask_mysqldb import MySQL
app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'absensi'
mysql = MySQL(app)

@app.route('/input', methods=['POST'])
def input():

        details = request.get_json()
        nama = details['nama']
        tanggal_lahir = details['tanggal_lahir']
        tempat_tinggal = details['tempat_tinggal']
        jabatan = details['jabatan']
        id = details['id']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO karyawan(nama, tanggal_lahir, tempat_tinggal, jabatan, id) VALUES (%s, %s, %s, %s, %s)", (nama, tanggal_lahir, tempat_tinggal, jabatan, id))
        mysql.connection.commit()
        cur.close()
        return make_response(jsonify(message = "sukses"), 200)
    

@app.route('/list')
def list():
   cur = mysql.connection.cursor()
   cur.execute('''SELECT * FROM karyawan''')
   row_headers=[x[0] for x in cur.description] #this will extract row headers
   rv = cur.fetchall()
   json_data=[]
   for result in rv:
        json_data.append(dict(zip(row_headers,result)))
   return json.dumps(json_data)

@app.route('/update/<int:id>', methods = ['POST'])
def ubah(id):
    cur = mysql.connection.cursor()
    details = request.get_json()
    nama = details['nama']
    tanggal_lahir = details['tanggal_lahir']
    tempat_tinggal = details['tempat_tinggal']
    jabatan = details['jabatan']
    cur.execute("""
       UPDATE karyawan
       SET nama=%s, tanggal_lahir=%s, tempat_tinggal=%s, jabatan=%s
       WHERE id=%s
    """, (nama, tanggal_lahir, tempat_tinggal, jabatan, id))

    mysql.connection.commit()

    return make_response(jsonify(message = "sukses update data"), 200)

@app.route('/delete/<int:id>', methods = ['GET'])
def delete(id):
    cur = mysql.connection.cursor()
    deletedata = "DELETE FROM karyawan WHERE id='%s'"%(id)
    cur.execute(deletedata)

    mysql.connection.commit()
    return make_response(jsonify(message = "sukses delete data"), 200)


if __name__ == '__main__':
    app.run(debug=True)