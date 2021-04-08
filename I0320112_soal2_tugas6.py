
#masukkan jumlah data
x = int(input('Masukkan jumlah data nilai:'))

nilai = []
jumlah = 0

#program
for i in range(0, x):
    list_nilai = int(input("Nilai siswa %d :" % (i + 1)))
    nilai.append(list_nilai)
    jumlah = jumlah + nilai[i]
    rata_rata = jumlah / x
print("Rata-rata nilai siswa adalah = %0.3f" % rata_rata)
