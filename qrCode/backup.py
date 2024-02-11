# Backup dari Application Generate qr Code
#  
# Apabila error bisa anda ambil file ini, namun App ini belum 100% jadi.......

import qrcode
from qrcode.main import QRCode
import json

with open('d:/produktif bu Tya/App/data.json', 'r') as file_json:
    file = json.load(file_json)
    
qr = QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)

nama = str(input('masukkan nama file : '))
namafile = str(input('masukkan file json : '))

if namafile not in file:
    print('Data tidak ada')
else:
    jsonSave = file[namafile]
    save = 'd:/produktif bu Tya/App/qrCode/img/' + nama + '.png'
    data = f'nomor induk : {jsonSave["nomor_induk"]} \n Nama: {jsonSave["nama"]} \n Kelas : {jsonSave["kelas"]} \n Jurusan : {jsonSave["jurusan"]}'
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    img.save(save)
    print('successs')
    
    
    
    
    
    
    
    
    
import PySimpleGUI as sg
from qrcode.main import QRCode
import json
import qrcode
import os

with open('d:/produktif bu Tya/App/data.json', 'r') as file_json:
    file = json.load(file_json)

dashboard = [
    [sg.Text('Create QR Code')],
    [sg.Text('Masukkan nama file : ', size=(15, 1)), sg.InputText(key='Nama')],
    [sg.Text('Masukkan lokasi file JSON : ', size=(15, 1)), sg.Combo(list(file.keys()), key='file')],
    [sg.Button('Generate now!'), sg.Exit()]
]

layout = sg.Window('Generate qrCode', dashboard)

def qrCodegenerate(nama, namaFile):
    qr = QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    
    jsonSave = file[namaFile]
    data = f'nomor induk : {jsonSave["nomor_induk"]} \n Nama: {jsonSave["nama"]} \n Kelas : {jsonSave["kelas"]} \n Jurusan : {jsonSave["jurusan"]}'

    save_dir = 'd:/produktif bu Tya/App/qrCode/img/'
    save_path = os.path.join(save_dir, f'{nama}.png')

    if not os.path.exists(save_dir):
        os.makedirs(save_dir)
        return

    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    img.save(save_path)

    return save_path

while True:
    event, values = layout.read()

    if event == sg.WINDOW_CLOSED or event == 'EXIT':
        break

    if event == 'Generate now!':
        nama = values['Nama']
        namaFile = values['file']

        if namaFile not in file:
            sg.popup('Data tidak ada')
        else:
            saved_path = qrCodegenerate(nama, namaFile)
            sg.popup('Berhasil membuat qrCode!')
            
    layout['Nama']('')
    layout['file']('')

layout.close()