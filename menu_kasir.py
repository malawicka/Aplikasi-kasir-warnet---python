import os
import getpass

def login():
    print("Login Yaa Mas dan Mbak ....")
    user = input("Isikan Username Anda : ")
    passwd = getpass.getpass("Isikan Password Anda : ")

    if user=='admin' and passwd=='admin1234' :
        os.system('cls')
        print("Anda Berhasil Login")
        input("Silahkan Tekan Sembarang Tombol")
        from paket import menu_utama
        
    else:
        os.system('cls')
        print("Anda Gagal Login")
login()