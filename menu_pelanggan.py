
class Pelanggan:
    def pelangganTetap(self):
        pel_tetap = 5000
        print("Anda Pelanggan Tetap")
        lama_main = int(input("Lama Jam Main Warnet = "))
        total_bayar = lama_main * pel_tetap
        if lama_main >= 5:
            total_bayar = round(total_bayar * 0.45)
        print("Total Bayar: Rp", total_bayar)

    def pelangganUmum(self):
        pel_umum = 7000
        print("Anda Pelanggan Umum")
        lama_main = int(input("Lama Jam Main Warnet = "))
        total_bayar = lama_main * pel_umum
        if lama_main >= 5:
            total_bayar = round(total_bayar * 0.3)
        print("Total Bayar: Rp", total_bayar)

