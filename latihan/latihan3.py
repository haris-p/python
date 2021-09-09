total = []

print("=" * 20)
print("Warung Babeh")
print("=" * 20)

def daftarbarang():
    print("No   :   Barang  :   Harga")
    print("1    :   Baju    :   28000")
    print("2    :   Celana  :   24000")
    print("3    :   Jaket   :   30000")

    kode = int(input("Masukan Kode Barang: "))
    if kode == 1:
        jumlah1 = int(input("Masukan Jumlah Barang: "))
        total1 = 28000 * jumlah1
        total.append(total1)
        tanya()
    elif kode == 2:
        jumlah2 = int(input("Masukan Jumlah Barang: "))
        total2 = 24000 * jumlah2
        total.append(total2)
        tanya()
    elif kode == 3:
        jumlah3 = int(input("Masukan Jumlah Barang"))
        total3 = 30000 * jumlah3
        total.append(total3)
        tanya()
    return

def tanya():
    print("=" * 20)
    print("Ada yang mau ditambah pencet y")
    print("Jika tidak Pencet t")
    print("="* 20)

    tanya = input("Y/T :")

    if tanya == "y":
        daftarbarang()
    elif tanya == "t":
        totalakhir()
    else:
        print("Kode yang anda masukan salah")

def totalakhir():
    for harga in total:
        print("Harga daftar barang :", sum(total))
        diskon = 0
        a = sum(total)
        if a >= 60000:
            diskon = a * 30/100
        else:
            diskon = 0

        print("Mendapatkan diskon: ", diskon)
        jumlahTotal = a - diskon
        print("Total :", jumlahTotal)
        print("=" * 20)
        bayar = int(input("Pembayaran: "))
        pajak = 200
        kembalian = (bayar - jumlahTotal) - pajak
        print("pajak: ", pajak)
        print("Kembalian", kembalian)
       

daftarbarang()