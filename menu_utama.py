import os
from paket.menu_pelanggan import Pelanggan
class MnUtama:

    def tampilkan_menu():
        print("=" * 40)
        print("SELAMAT DATANG DI WARNET BANG GUNS")
        print("=" * 40)
        print("")
        print("1. Pilih, Jika Pembayaran Pelanggan Tetap")
        print("2. Pilih, Jika Pembayaran Pelanggan Umum")
        print("3. Keluar")

   
    def utama():
        MnUtama.tampilkan_menu()
        pilihan = input("Isikan Pilihan Anda: ")

        if pilihan == '1':
            Pelanggan().pelangganTetap()
        elif pilihan == '2':
            Pelanggan().pelangganUmum()
        elif pilihan == '3':
            print("Terima kasih.")
        else:
            print("Pilihan Anda tidak valid.")

        print("")
        input("Tekan Enter untuk melanjutkan...")
        
        if pilihan != '3':
            os.system('cls')
            MnUtama.utama()

        os.system('cls')
MnUtama.utama()
