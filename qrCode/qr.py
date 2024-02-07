import PySimpleGUI as sg
from qrcode.main import QRCode
import json
import qrcode
import os

#import data from json

with open('d:/produktif bu Tya/App/data.json', 'r') as file_json:
    file = json.load(file_json)

# tampilan awal Aplikasi

dashboard = [
    [sg.Text('Create QR Code')],
    [sg.Text('Masukkan nama file : ', size=(15, 1)), sg.InputText(key='Nama')],
    [sg.Text('Masukkan lokasi file JSON : ', size=(15, 1)), sg.Combo(list(file.keys()), key='file')],
    [sg.Button('Generate now!'), sg.Exit()]
]

layout = sg.Window('Generate qrCode', dashboard)

# Function Generate qr Code

def qrCodegenerate(nama, namaFile):
    
    qr = QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    
    # mencari nama file yang di pilih di  =>  Masukkan lokasi file JSON nya
    jsonSave = file[namaFile]
    
    # Mengatasi tampilan saat qr Code di scan agar lebih rapi
    data = f'Nomor Induk : {jsonSave["nomor_induk"]} \n Nama: {jsonSave["nama"]} \n Kelas : {jsonSave["kelas"]} \n Jurusan : {jsonSave["jurusan"]}'
    
    # digunakan untuk menyimpan data qr Code yang telah dibuat
    save_dir = 'd:/produktif bu Tya/App/qrCode/img/'
    
    # digunakan untuk menyimpan data qr Code dengan nama yang telah diketik di atas => Masukkan nama file
    save_path = os.path.join(save_dir, f'{nama}.png')

    # Berfungsi agar apabila save_dir tidak ada, maka langsung otomatis membuat folder baru sesuai dengan di variabel save_dir
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)

    # Membuat qr Code
    qr.add_data(data)
    
    qr.make(fit=True)
    
    # Membuat tampilan qr Code 
    img = qr.make_image(fill_color="black", back_color="white")
    
    # Menyimpan qr Code sesuai yang di atas  => save_dir
    img.save(save_path)

    return save_path

# Melooping Aplikasi
while True:
    # Membuat variabel baru dengan membaca Aplikasinya
    event, values = layout.read()
    
    # Apabila menekan tombol EXIT maka Aplikasi berhenti
    if event == sg.WINDOW_CLOSED or event == 'EXIT':
        break

    # Apabila menekan tombol Generate Now maka akan membuat qr Codenya
    if event == 'Generate now!':
        
        # Mengambil Value / key dari input di atas
        nama = values['Nama']
        namaFile = values['file']

        # Apabila nama file / => 'Masukkan lokasi file JSON' tidak ada 
        if namaFile not in file:
            sg.popup('Data tidak ada')
        # Apabila nama file ada
        else:
            # Menyimpan qr Code
            saved_path = qrCodegenerate(nama, namaFile)
            
            # Alert/pop up apabila berhasi;
            sg.popup('Berhasil membuat qrCode!')
            
            # Mereset Form setelah membuat qr Code nya
            layout['Nama'].update('')
            layout['file'].update('')

layout.close()
