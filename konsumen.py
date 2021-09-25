from flask import Flask, render_template, request
from flask_mysqldb import MySQL
app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'absensi'
mysql = MySQL(app)
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == "POST":
        details = request.form
        nama = details['nama']
        tanggal_lahir = details['tanggal_lahir']
        tempat_tinggal = details['tempat_tinggal']
        jabatan = details['jabatan']
        id = details['id']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO karyawan(nama, tanggal_lahir, tempat_tinggal, jabatan, id) VALUES (%s, %s, %s, %s, %s)", (nama, tanggal_lahir, tempat_tinggal, jabatan, id))
        mysql.connection.commit()
        cur.close()
        return 'sukses'
    return render_template('index.html')

@app.route("/update/<id>", methods=['GET', 'PUT', 'DELETE'])
def author():
    if request.method == 'GET':
        return 

if __name__ == '__main__':
    app.run(debug=True)