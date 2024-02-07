from flask import Flask, render_template, request
from qrcode.main import QRCode
import json
import qrcode
import os

with open('d:/produktif bu Tya/App/data.json', 'r') as file_json:
    file = json.load(file_json)

app = Flask(__name__, static_url_path='/static')

@app.route('/')
def index():
    return render_template('index.html', file=file)

@app.route('/templates', methods=['POST', 'GET'])
def qr():
    nama = request.form.get('name')
    nama_file = request.form.get('select')
    
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    
    jsonSave = file[nama_file]
    data = f'nomor induk : {jsonSave["nomor_induk"]} \n Nama: {jsonSave["nama"]} \n Kelas : {jsonSave["kelas"]} \n Jurusan : {jsonSave["jurusan"]}'

    save_dir = 'd:/produktif bu Tya/App/qrCode/img/'
    save_path = os.path.join(save_dir, f'{nama}.png')

    if not os.path.exists(save_dir):
        os.makedirs(save_dir)

    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    img.save(save_path)

    return render_template('db.html', file_path=save_path, nama=nama)

if __name__ == '__main__':
    app.run(debug=True)