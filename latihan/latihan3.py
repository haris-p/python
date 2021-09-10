

total = []
print("=" * 20)
print("Warung Babeh")
print("=" * 20)

def daftarbarang():
    print("No   :   Daftar Barang   :   Harga")
    print("1    :   Mild            :   25000")
    print("2    :   Filter          :   18000")
    print("3    :   Kretek          :   17000")
    print("=" * 20)

    kode = int(input("Masukan Kode Barang: "))
    if kode == 1:
        jumlah1 = int(input("Masukan Jumlah Barang: "))
        total1 = jumlah1 * 25000
        total.append(total1)
        tanya()
    elif kode == 2:
        jumlah2 = int(input("Masukan Jumlah Barang: "))
        total2 = jumlah2 * 18000
        total.append(total2)
        tanya()
    elif kode == 3:
        jumlah3 = int(input("Masukan Jumlah Barang: "))
        total3 = jumlah3 * 17000
        total.append(total3)
        tanya()
        return

def tanya():
    print("=" * 20)
    pertanyaan = input("Ada yang mau ditambahkan [y/t] :")

    if pertanyaan == "y":
        daftarbarang()
    elif pertanyaan == "t":
        hasilhitung()
    else:
        print("Kode yang anda masukan salah")

def hasilhitung():
    for harga in total:
        print("Total Barang: ", sum(total))
        diskon = 0
        a = sum(total)

        if a >= 30000:
            diskon = a * 10/100
        else:
            diskon = 0

        pajak = 0
        if a >= 20000:
            pajak = 3000
        else:
            pajak = 0

        print("=" * 20)
        print("diskon :", diskon)
        print("Pajak :", pajak)
        totalkeseluruhan = (a - diskon) + pajak
        print("Total Keseluruhan: ",totalkeseluruhan)
        print("=" * 20)
        pembayaran = int(input("Masukan Pembayaran: "))
        bayar = (pembayaran - totalkeseluruhan)
        print("Kembalian :", bayar)
        break

daftarbarang()